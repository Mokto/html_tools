use kuchiki::{traits::TendrilSink, NodeRef};
use pyo3::prelude::*;

const REMOVE_TAGS: [&'static str; 22] = [
    "script",
    "style",
    "noscript",
    "#coiOverlay",
    ".CookiesOK",
    "#closeCookieBanner",
    ".CookieBanner-button",
    "#nts-set-cookie",
    ".cc_btn_accept_all",
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
];

const PICK_TAGS: [&'static str; 6] = ["h1", "h2", "h3", "h4", "h5", "h6"];

#[pyfunction]
fn parse_html(html: String) -> PyResult<String> {
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

    let mut result: Vec<String> = vec![];

    for tag in PICK_TAGS {
        let mut text: Vec<String> = get_text_and_remove(&document, tag)
            .iter()
            // .filter(|x| count_words(x.as_str()) < 200)
            .take(30)
            .cloned()
            .collect();

        result.append(&mut text)
    }

    let mut paragraphs: Vec<String> = get_text_and_remove(&document, "p");
    paragraphs.sort_by(|a, b| count_words(b).cmp(&count_words(a)));

    let mut paragraphs: Vec<String> = paragraphs
        .iter()
        .filter(|x| count_words(x.as_str()) > 2)
        .map(|x| x.split(". "))
        .flatten()
        .map(|x| x.split("! "))
        .flatten()
        .map(|x| x.split("? "))
        .flatten()
        .map(|x| x.to_string())
        .filter(|x| count_words(x.as_str()) < 128)
        .take(30)
        .collect();

    // println!("COUCOU");
    // println!("{:?}", paragraphs);

    result.append(&mut paragraphs);
    // println!("{:?}", text);
    // .cloned()
    // .collect();
    // let document_str = document.text_contents();

    // let mut finder = LinkFinder::new();
    // finder.url_must_have_scheme(false);
    // let links: Vec<_> = finder.links(document_str.as_str()).collect();

    // for link in links {
    //     document_str.replace(link.as_str(), "");
    //     // println!("{:?}", link.as_str());
    // }

    // let beautified = document
    //     .text_contents()
    //     .split("\n")
    //     .map(|n| n.replace("\t", "").trim().to_string())
    //     .filter(|n| !n.is_empty())
    //     .map(|n| trim_punctuation(&n))
    //     .collect::<Vec<String>>()
    //     .join("\n");

    // println!("{}", beautified);

    Ok(result
        // .iter()
        // .filter(|n| count_words(n) > 1)
        // .collect()
        .join("\n"))
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
    m.add_function(wrap_pyfunction!(parse_html, m)?)?;
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
