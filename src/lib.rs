use std::collections::HashMap;

use kuchiki::{traits::TendrilSink, NodeRef};
use linkify::{LinkFinder, LinkKind};
use pyo3::prelude::*;
use regex::{Regex, RegexBuilder};

const REMOVE_TAGS: [&'static str; 27] = [
    // scripts/styles
    "script",
    "style",
    "noscript",
    // COOKIE BANNERS
    "#coiOverlay",
    ".CookiesOK",
    "#closeCookieBanner",
    ".CookieBanner-button",
    "#nts-set-cookie",
    ".cc_btn_accept_all",
    ".cookies",
    ".noticeCookiesContent .CustomDismissCtrl",
    ".cookie-consent .cookie-btn",
    "#accept-cookies",
    "#cookie_button_agree",
    "#cookies-agreement #agree-button",
    "#cookielayer .action-btn",
    ".cookie.nag .close",
    "#__tealiumGDPRecModal #consent_prompt_submit",
    ".gdpr__button",
    ".eu-cookie-compliance-agree-button",
    ".cookie-notification .js-cookie-notification-hide",
    ".js-accept-cookie-policy",
    "#moove_gdpr_cookie_info_bar",
    ".pea_cook_wrapper",
    // testimonials
    ".testimonial",
    ".testimonial-text",
    ".pwr-testimonial__quote", // hubspot
];

const PICK_TAGS: [&'static str; 6] = ["h1", "h2", "h3", "h4", "h5", "h6"];

#[pyfunction]
fn get_sentences(html: String, stop_word: String) -> PyResult<HashMap<String, Vec<String>>> {
    let mut result = HashMap::new();

    let document = kuchiki::parse_html().one(html);

    for tag in REMOVE_TAGS {
        remove_tag(&document, tag);
    }

    if true {
        remove_tag(&document, "header");
        remove_tag(&document, "nav");
        remove_tag(&document, ".header");
        remove_tag(&document, ".header-hero");
    }

    if true {
        remove_tag(&document, "footer");
        remove_tag(&document, ".footer");
        remove_tag(&document, ".footer-hero");
    }

    let stop_word_regex = RegexBuilder::new(stop_word.as_str())
        .case_insensitive(true)
        .build()
        .expect("Invalid Regex");

    for tag in PICK_TAGS {
        let text: Vec<String> = get_text_and_remove(&document, tag)
            .iter()
            .cloned()
            .collect();

        result.insert(tag.to_string(), apply(text, stop_word_regex.clone()));
    }

    let mut paragraphs: Vec<String> = get_text_and_remove(&document, "p");
    paragraphs.sort_by(|a, b| count_words(b).cmp(&count_words(a)));

    let paragraphs: Vec<String> = paragraphs
        .iter()
        .filter(|x| count_words(x.as_str()) > 2)
        .map(|x| x.split(". "))
        .flatten()
        .map(|x| x.split("! "))
        .flatten()
        .map(|x| x.split("? "))
        .flatten()
        .map(|x| x.to_string())
        // .filter(|x| count_words(x.as_str()) < 128)
        // .take(30)
        .collect();

    result.insert("p".to_string(), apply(paragraphs, stop_word_regex.clone()));

    let description = get_description(&document);
    if description.is_some() {
        result.insert(
            "description".to_string(),
            vec![description.clone().unwrap()],
        );
    }

    // Keywords
    let keywords = get_keywords(&document);
    if keywords.is_some() {
        result.insert("keywords".to_string(), vec![keywords.unwrap().to_string()]);
    }

    result.insert("all".to_string(), vec![document.text_contents()]);

    Ok(result)
}

#[pyfunction]
fn get_links(html: String) -> PyResult<Vec<String>> {
    let mut finder = LinkFinder::new();
    finder.kinds(&[LinkKind::Url]);
    let links = finder.links(html.as_str());
    let links = links.map(|x| x.as_str().to_string());
    Ok(links.collect::<Vec<String>>())
}

#[pyfunction]
fn get_href_attributes(html: String) -> PyResult<Vec<String>> {
    let document = kuchiki::parse_html().one(html);
    // let mut links: Vec<String> = vec![];

    let links: Vec<String> = document
        .select("a")
        .unwrap()
        // .collect()
        .map(|x| {
            let attributes = x.attributes.borrow();
            let href = attributes.get("href");
            if href.is_none() {
                return "".to_string();
            }
            href.unwrap().to_string()
        })
        .collect();

    Ok(links)
}

#[pyfunction]
fn get_emails(html: String) -> PyResult<Vec<String>> {
    let mut finder = LinkFinder::new();
    finder.kinds(&[LinkKind::Email]);
    let links = finder.links(html.as_str());
    let links = links.map(|x| x.as_str().to_string());
    Ok(links.collect::<Vec<String>>())
}

#[pyfunction]
fn html_contents(html: String) -> PyResult<String> {
    let document = kuchiki::parse_html().one(html);
    for tag in REMOVE_TAGS {
        remove_tag(&document, tag);
    }
    Ok(document.to_string())
}

#[pyfunction]
fn tag_html_contents(html: String, tag: String) -> PyResult<String> {
    let document = kuchiki::parse_html().one(html);
    let document = document.select_first(tag.as_str());
    let res = match document {
        Ok(v) => v.as_node().to_string(),
        Err(_) => "".to_string(),
    };

    Ok(res)
}

fn apply(sentences: Vec<String>, stop_word_regex: Regex) -> Vec<String> {
    sentences
        .iter()
        .map(|n| {
            stop_word_regex
                .replace_all(&n, "")
                .to_string()
                .trim()
                .to_string()
        })
        .filter(|n| !n.to_lowercase().contains("cookie") && !n.contains("©") && count_words(n) > 0)
        .collect()
}

fn get_description(document: &NodeRef) -> Option<String> {
    let tag_nodes = document.select("meta").unwrap();
    for tag_node in tag_nodes.collect::<Vec<_>>() {
        let attributes = tag_node.attributes.borrow();
        let name_attribute = attributes.get("name").unwrap_or("");
        if name_attribute == "description" || name_attribute == "og:description" {
            let content_attribute = attributes.get("content").unwrap_or("");
            if !content_attribute.is_empty() {
                return Some(content_attribute.to_string());
            }
        }
    }
    return None;
}
fn get_keywords(document: &NodeRef) -> Option<String> {
    let tag_nodes = document.select("meta").unwrap();
    for tag_node in tag_nodes.collect::<Vec<_>>() {
        let attributes = tag_node.attributes.borrow();
        let name_attribute = attributes.get("name").unwrap_or("");
        if name_attribute == "keywords" {
            let content_attribute = attributes.get("content").unwrap_or("");
            if !content_attribute.is_empty() {
                return Some(content_attribute.to_string());
            }
        }
    }
    return None;
}

fn get_text_and_remove(document: &NodeRef, tag: &str) -> Vec<String> {
    let mut result: Vec<String> = vec![];
    let tag_nodes = document.select(tag).unwrap();
    for tag_node in tag_nodes.collect::<Vec<_>>() {
        let text = trim_whitespace(tag_node.text_contents().as_str());
        if !text.is_empty() {
            result.push(trim_whitespace(tag_node.text_contents().as_str()));
        }
        let as_node = tag_node.as_node();
        as_node.detach();
    }
    return result;
}

fn remove_tag(document: &NodeRef, tag: &str) {
    let tag_nodes = document.select(tag).unwrap();
    for tag_node in tag_nodes.collect::<Vec<_>>() {
        let as_node = tag_node.as_node();
        as_node.detach();
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn html_parsing_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_emails, m)?)?;
    m.add_function(wrap_pyfunction!(get_links, m)?)?;
    m.add_function(wrap_pyfunction!(html_contents, m)?)?;
    m.add_function(wrap_pyfunction!(tag_html_contents, m)?)?;
    m.add_function(wrap_pyfunction!(get_sentences, m)?)?;
    m.add_function(wrap_pyfunction!(get_href_attributes, m)?)?;
    Ok(())
}

fn trim_whitespace(s: &str) -> String {
    let mut result = String::with_capacity(s.len());
    s.split_whitespace().for_each(|w| {
        if !result.is_empty() {
            result.push(' ');
        }
        result.push_str(w);
    });
    if result.is_empty() {
        return result;
    }
    trim_punctuation(result.as_str())
}

fn trim_punctuation(n: &str) -> String {
    let last_char = n.chars().last().unwrap();
    if last_char == '.' || last_char == ',' {
        let mut chars = n.chars();
        chars.next_back();
        return chars.as_str().to_string();
    }
    return n.to_string();
}

fn count_words(s: &str) -> usize {
    let mut total = 0;
    let mut previous = char::MAX;
    for c in s.chars() {
        // If previous char is whitespace, we are on a new word.
        if previous.is_ascii_whitespace() {
            // New word has alphabetic, digit or punctuation start.
            if c.is_ascii_alphabetic() || c.is_ascii_digit() || c.is_ascii_punctuation() {
                total += 1;
            }
        }
        // Set previous.
        previous = c;
    }
    if s.len() >= 1 {
        total += 1
    }
    total
}
