use ndarray::{Array1, Array2};
use pyo3::prelude::*;
use std::collections::BTreeSet;
use unicode_segmentation::UnicodeSegmentation;

const STOP_WORDS: [&'static str; 580] = [
    "onto",
    "during",
    "while",
    "l",
    "appreciate",
    "forth",
    "could",
    "he'll",
    "able",
    "each",
    "eg",
    "would",
    "despite",
    "aside",
    "haven't",
    "you'll",
    "wherein",
    "otherwise",
    "saying",
    "someone",
    "thanks",
    "unto",
    "mean",
    "cannot",
    "indeed",
    "described",
    "can",
    "seems",
    "most",
    "was",
    "you're",
    "exactly",
    "actually",
    "consequently",
    "that's",
    "ever",
    "seeming",
    "any",
    "we'll",
    "behind",
    "thoroughly",
    "normally",
    "novel",
    "last",
    "ought",
    "uucp",
    "believe",
    "comes",
    "than",
    "amongst",
    "theirs",
    "ex",
    "our",
    "follows",
    "thence",
    "has",
    "everything",
    "sometimes",
    "they're",
    "maybe",
    "anywhere",
    "anyhow",
    "herself",
    "quite",
    "doesn't",
    "indicated",
    "specified",
    "different",
    "relatively",
    "regardless",
    "hence",
    "f",
    "ok",
    "mainly",
    "looking",
    "y",
    "not",
    "shall",
    "must",
    "use",
    "edu",
    "vs",
    "namely",
    "before",
    "see",
    "six",
    "liked",
    "if",
    "nevertheless",
    "gone",
    "being",
    "myself",
    "of",
    "inward",
    "does",
    "very",
    "too",
    "themselves",
    "think",
    "available",
    "it",
    "eight",
    "down",
    "beside",
    "few",
    "sup",
    "already",
    "clearly",
    "she",
    "try",
    "co",
    "hadn't",
    "ain't",
    "etc",
    "x",
    "yes",
    "become",
    "yourselves",
    "consider",
    "how",
    "whereas",
    "across",
    "w",
    "says",
    "per",
    "other",
    "its",
    "changes",
    "mustn't",
    "out",
    "e",
    "uses",
    "i'll",
    "t's",
    "hers",
    "keep",
    "should",
    "i'd",
    "after",
    "that",
    "thank",
    "one",
    "knows",
    "lately",
    "serious",
    "taken",
    "these",
    "latter",
    "whom",
    "you've",
    "got",
    "took",
    "howbeit",
    "over",
    "according",
    "let",
    "particularly",
    "weren't",
    "awfully",
    "alone",
    "u",
    "seen",
    "yet",
    "can't",
    "me",
    "never",
    "he'd",
    "keeps",
    "between",
    "overall",
    "twice",
    "others",
    "possible",
    "known",
    "z",
    "a",
    "secondly",
    "sensible",
    "ignored",
    "immediate",
    "tends",
    "ones",
    "will",
    "towards",
    "throughout",
    "viz",
    "nearly",
    "apart",
    "i've",
    "okay",
    "wouldn't",
    "anyway",
    "same",
    "until",
    "your",
    "probably",
    "although",
    "used",
    "along",
    "this",
    "associated",
    "below",
    "they've",
    "enough",
    "done",
    "corresponding",
    "an",
    "be",
    "willing",
    "thus",
    "say",
    "am",
    "rd",
    "anyone",
    "you'd",
    "both",
    "need",
    "them",
    "who's",
    "sure",
    "thereupon",
    "indicate",
    "since",
    "when",
    "go",
    "why",
    "yourself",
    "soon",
    "four",
    "non",
    "lest",
    "brief",
    "currently",
    "much",
    "or",
    "wonder",
    "whenever",
    "besides",
    "they",
    "for",
    "ie",
    "aren't",
    "from",
    "to",
    "necessary",
    "us",
    "none",
    "may",
    "but",
    "once",
    "downwards",
    "thats",
    "tell",
    "anybody",
    "d",
    "reasonably",
    "sorry",
    "itself",
    "trying",
    "we'd",
    "appear",
    "placed",
    "they'll",
    "meanwhile",
    "perhaps",
    "him",
    "three",
    "elsewhere",
    "b",
    "look",
    "regards",
    "her",
    "followed",
    "g",
    "right",
    "little",
    "gives",
    "v",
    "r",
    "doing",
    "obviously",
    "in",
    "sub",
    "come",
    "upon",
    "using",
    "where's",
    "himself",
    "help",
    "together",
    "going",
    "especially",
    "first",
    "why's",
    "as",
    "hopefully",
    "certain",
    "he's",
    "just",
    "where",
    "isn't",
    "above",
    "new",
    "how's",
    "cant",
    "against",
    "thorough",
    "she'd",
    "on",
    "herein",
    "following",
    "rather",
    "way",
    "instead",
    "self",
    "whoever",
    "best",
    "well",
    "happens",
    "many",
    "therefore",
    "whence",
    "we",
    "everyone",
    "zero",
    "considering",
    "tried",
    "wants",
    "p",
    "beforehand",
    "whole",
    "couldn't",
    "whether",
    "allow",
    "there's",
    "else",
    "far",
    "and",
    "indicates",
    "unfortunately",
    "somewhere",
    "neither",
    "i'm",
    "concerning",
    "they'd",
    "like",
    "beyond",
    "wish",
    "insofar",
    "into",
    "unless",
    "away",
    "something",
    "mostly",
    "let's",
    "least",
    "nowhere",
    "example",
    "given",
    "particular",
    "there",
    "a's",
    "nothing",
    "please",
    "my",
    "really",
    "goes",
    "went",
    "with",
    "o",
    "whatever",
    "almost",
    "own",
    "when's",
    "seven",
    "were",
    "through",
    "value",
    "seriously",
    "nobody",
    "t",
    "another",
    "no",
    "either",
    "within",
    "unlikely",
    "came",
    "que",
    "outside",
    "been",
    "all",
    "whereafter",
    "accordingly",
    "hasn't",
    "then",
    "nd",
    "former",
    "somebody",
    "which",
    "fifth",
    "n",
    "so",
    "k",
    "thanx",
    "third",
    "ltd",
    "specify",
    "seem",
    "entirely",
    "hereafter",
    "somehow",
    "et",
    "five",
    "shouldn't",
    "again",
    "better",
    "more",
    "later",
    "want",
    "hereupon",
    "therein",
    "merely",
    "except",
    "hither",
    "containing",
    "re",
    "what's",
    "looks",
    "among",
    "ours",
    "sometime",
    "q",
    "plus",
    "became",
    "inasmuch",
    "specifying",
    "th",
    "regarding",
    "his",
    "seemed",
    "c",
    "ask",
    "furthermore",
    "around",
    "have",
    "thru",
    "at",
    "thereby",
    "gotten",
    "becoming",
    "those",
    "we've",
    "hello",
    "under",
    "certainly",
    "definitely",
    "old",
    "are",
    "truly",
    "who",
    "don't",
    "second",
    "allows",
    "didn't",
    "toward",
    "inc",
    "qv",
    "know",
    "tries",
    "sent",
    "had",
    "it's",
    "shan't",
    "their",
    "cause",
    "whereupon",
    "also",
    "some",
    "we're",
    "kept",
    "less",
    "yours",
    "here's",
    "m",
    "getting",
    "wherever",
    "anyways",
    "respectively",
    "anything",
    "saw",
    "though",
    "needs",
    "welcome",
    "h",
    "it'd",
    "take",
    "com",
    "everywhere",
    "she's",
    "often",
    "somewhat",
    "moreover",
    "it'll",
    "provides",
    "always",
    "c's",
    "about",
    "wasn't",
    "oh",
    "s",
    "selves",
    "here",
    "un",
    "nor",
    "whose",
    "nine",
    "he",
    "latterly",
    "causes",
    "still",
    "formerly",
    "greetings",
    "won't",
    "useful",
    "by",
    "the",
    "get",
    "whither",
    "i",
    "having",
    "such",
    "you",
    "she'll",
    "do",
    "contains",
    "inner",
    "various",
    "asking",
    "up",
    "everybody",
    "might",
    "without",
    "however",
    "likely",
    "noone",
    "seeing",
    "theres",
    "presumably",
    "ourselves",
    "via",
    "hardly",
    "what",
    "gets",
    "hereby",
    "because",
    "name",
    "afterwards",
    "now",
    "usually",
    "several",
    "even",
    "near",
    "course",
    "thereafter",
    "every",
    "said",
    "becomes",
    "off",
    "further",
    "appropriate",
    "only",
    "j",
    "two",
    "c'mon",
    "contain",
    "whereby",
    "did",
    "next",
    "hi",
    "is",
];

/// Formats the sum of two numbers as string.
#[pyfunction]
fn parse_html(a: String) -> PyResult<String> {
    // summarize
    Ok(summarize(&a, &STOP_WORDS, 10))
}

/// A Python module implemented in Rust.
#[pymodule]
fn html_parsing_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_html, m)?)?;
    Ok(())
}

pub fn summarize(text: &str, stop_words: &[&str], num_sentence: usize) -> String {
    let sentences = text.unicode_sentences().collect::<Vec<&str>>();
    if num_sentence >= sentences.len() {
        return text.to_string();
    }
    let mut sentences_and_words = vec![];
    sentences.iter().for_each(|&sentence| {
        let words = split_into_words(sentence);
        sentences_and_words.push(words);
    });
    let matrix = build_similarity_matrix(&sentences_and_words, stop_words);
    let ranks = calculate_sentence_rank(&matrix);
    let mut sorted_ranks = ranks.clone();
    sorted_ranks.sort_by(|a, b| b.partial_cmp(a).unwrap());
    let least_rank = sorted_ranks[num_sentence + 1];
    let mut result: Vec<&str> = vec![];
    let mut included_count = 0;
    for i in 0..sentences.len() {
        if ranks[i] >= least_rank {
            included_count = included_count + 1;
            result.push(sentences[i]);
        }
        if included_count == num_sentence {
            break;
        }
    }
    result.join("")
}

fn get_all_words_lc<'a>(sentence1: &[&'a str], sentence2: &[&'a str]) -> BTreeSet<String> {
    let mut all_words: BTreeSet<String> = BTreeSet::new();

    sentence1.iter().for_each(|w| {
        all_words.insert(w.to_lowercase());
    });

    sentence2.iter().for_each(|w| {
        all_words.insert(w.to_lowercase());
    });
    return all_words;
}

///
/// Retrieve a sentence vector based on the frequency of words that appears in the all_words_lc set.
/// all_words_lc should be a sorted set of lower cased words
/// The size of the resulting vector is the same as the all_words_lc set
/// stop_words are skipped
///
fn get_sentence_vector(
    sentence: &[&str],
    all_words_lc: &BTreeSet<String>,
    stop_words: &[&str],
) -> Vec<usize> {
    let mut vector: Vec<usize> = vec![0; all_words_lc.len()];
    for word in sentence {
        let word_lc = word.to_lowercase();
        if !stop_words.contains(&word_lc.as_str()) {
            let index = all_words_lc.iter().position(|x| x.eq(&word_lc)).unwrap();
            vector[index] += 1;
        }
    }
    return vector;
}

///
/// Calculates the cosine distance between two vectors
/// Refer to [YouTube](https://www.youtube.com/watch?v=3X0wLRwU_Ws)
///
fn cosine_distance(vec1: &Vec<usize>, vec2: &Vec<usize>) -> f64 {
    let dot_product = dot_product(vec1, vec2);
    let root_sum_square1 = root_sum_square(vec1);
    let root_sum_square2 = root_sum_square(vec2);
    return dot_product as f64 / (root_sum_square1 * root_sum_square2);
}

fn root_sum_square(vec: &Vec<usize>) -> f64 {
    let mut sum_square = 0;
    for i in 0..vec.len() {
        sum_square += vec[i] * vec[i];
    }
    (sum_square as f64).sqrt()
}

fn dot_product(vec1: &Vec<usize>, vec2: &Vec<usize>) -> usize {
    let delta = vec1.len() - vec2.len();
    let shortest_vec = match delta {
        d if d < 0 => vec1,
        d if d > 0 => vec2,
        _ => vec1,
    };
    let mut dot_product = 0;
    for i in 0..shortest_vec.len() {
        dot_product += vec1[i] * vec2[i];
    }
    dot_product
}

fn sentence_similarity(s1: &[&str], s2: &[&str], stop_words: &[&str]) -> f64 {
    let all_words = get_all_words_lc(s1, s2);
    let v1 = get_sentence_vector(s1, &all_words, stop_words);
    let v2 = get_sentence_vector(s2, &all_words, stop_words);
    1.0 - cosine_distance(&v1, &v2)
}

///
/// Calculate a similarity matrix for the given sentences.
/// Returns a 2-D array M_i,j such that for all 'j', sum(i, M_i,j) = 1
/// We take a leap of faith here and assume that cosine similarity is similar to the probability
/// that a sentence is important for summarization
///
fn build_similarity_matrix(sentences: &Vec<Vec<&str>>, stop_words: &[&str]) -> Array2<f64> {
    let len = sentences.len();
    let mut matrix = Array2::<f64>::zeros((len, len));
    let mut sum_column: Vec<f64> = vec![0.0; len];
    for i in 0..len {
        for j in 0..len {
            if i == j {
                continue;
            }
            matrix[[i, j]] =
                sentence_similarity(sentences[i].as_slice(), sentences[j].as_slice(), stop_words);
        }
    }
    // at this point we have the cosine similarity of each sentence.
    // take a leap of faith and assume that the cosine similarity is the probability that a sentence
    // is important for summarization.
    // We do this by normalizing the matrix along the column. The column values should add up to 1.
    for j in 0..len {
        let mut sum: f64 = 0.0;
        for i in 0..len {
            if i == j {
                continue;
            }
            sum += matrix[[i, j]];
        }
        sum_column[j] = sum;
    }
    for i in 0..len {
        for j in 0..len {
            if i == j {
                continue;
            }
            matrix[[i, j]] = matrix[[i, j]] / sum_column[j];
        }
    }
    matrix
}

///
/// Calculate a sentence rank similar to a page rank.
/// Please refer to [PageRank](https://en.wikipedia.org/wiki/PageRank) for more details.
///
fn calculate_sentence_rank(similarity_matrix: &Array2<f64>) -> Vec<f64> {
    let num_sentence = similarity_matrix.shape()[1];
    let threshold = 0.001;
    // Initialize a vector with the same value 1/number of sentences. Uniformly distributed across
    // all sentences. NOTE: perhaps we can make some sentences more important than the rest?
    let initial_vector: Vec<f64> = vec![1.0 / num_sentence as f64; num_sentence];
    let mut result = Array1::from(initial_vector);
    let mut prev_result = result.clone();
    let damping_factor = 0.85;
    let initial_m =
        damping_factor * similarity_matrix + (1.0 - damping_factor) / num_sentence as f64;
    loop {
        result = initial_m.dot(&result);
        let delta = &result - &prev_result;
        let mut converged = true;
        for i in 0..delta.len() {
            if delta[i] > threshold {
                converged = false;
                break;
            }
        }
        if converged {
            break;
        }
        prev_result = result.clone();
    }
    result.into_raw_vec()
}

fn split_into_words(sentence: &str) -> Vec<&str> {
    let mut result = vec![];
    let words = sentence.unicode_words();
    for word in words {
        result.push(word);
    }
    result
}
