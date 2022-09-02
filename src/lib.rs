use boilerpipe::parse_document;
use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn parse_html(a: String) -> PyResult<String> {
    Ok(parse_document(&a).content().to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn html_parsing_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_html, m)?)?;
    Ok(())
}
