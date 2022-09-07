use kuchiki::{traits::TendrilSink, NodeRef};
use pyo3::prelude::*;

const REMOVE_TAGS: [&'static str; 21] = [
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
];

#[pyfunction]
fn parse_html(html: String) -> PyResult<String> {
    // summarize
    println!("COUCOU");
    let document = kuchiki::parse_html().one(html);

    for tag in REMOVE_TAGS {
        remove_tag(&document, tag);
    }

    if true {
        remove_tag(&document, "header");
    }

    if true {
        remove_tag(&document, "footer");
    }

    // let document_str = document.text_contents();

    // let mut finder = LinkFinder::new();
    // finder.url_must_have_scheme(false);
    // let links: Vec<_> = finder.links(document_str.as_str()).collect();

    // for link in links {
    //     document_str.replace(link.as_str(), "");
    //     // println!("{:?}", link.as_str());
    // }

    let beautified = document
        .text_contents()
        .split("\n")
        .filter(|n| !n.replace("\t", "").trim().is_empty())
        .collect::<Vec<&str>>()
        .join("\n");

    // println!("{}", beautified);

    Ok(beautified)
}

fn remove_tag(document: &NodeRef, tag: &str) {
    let scripts = document.select(tag).unwrap();
    for script in scripts.collect::<Vec<_>>() {
        let as_node = script.as_node();
        as_node.detach();
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn html_parsing_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_html, m)?)?;
    Ok(())
}
