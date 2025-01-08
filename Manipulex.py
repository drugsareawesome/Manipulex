import re
from textblob import TextBlob

# Define patterns and keywords for gaslighting and manipulation detection
GASLIGHTING_PATTERNS = [
    r"\b(you always|you never)\b",  # Absolute statements
    r"\b(it's all in your head|you're imagining things)\b",
    r"\b(you're too sensitive|you're overreacting)\b",
    r"\b(that never happened|I never said that)\b",
    r"\b(why can't you just|you should be grateful)\b",
    r"\b(you're being paranoid|nobody else has a problem with this)\b",
    r"\b(why can't you just let it go|you're making a big deal out of nothing)\b",
    r"\b(if you loved me, you would|after all I’ve done for you)\b",
    r"\b(you’d be nothing without me|I know what’s best for you)\b",
    r"\b(you’re remembering it wrong|stop being so emotional)\b",
    r"\b(it’s not a big deal|you’re making things up)\b",
]

MANIPULATION_KEYWORDS = [
    "must", "need", "should", "guarantee", "urgent", "important",
    "deserve", "owe", "proven", "obviously", "clearly",
    "fear", "guilt", "obligation", "dependent",
    "always", "never", "fault", "blame", "responsibility", "mistake",
    "risk", "danger", "lose", "ruin", "stupid", "incapable", "weak"
]

ADDITIONAL_MANIPULATIVE_PHRASES = [
    "after everything I’ve done for you",
    "you should be ashamed of yourself",
    "you owe me this",
    "if you really cared about me, you would",
    "don’t you trust me",
    "this is for your own good",
    "you’ll thank me later",
    "you don’t have a choice",
    "I’m the only one who can help you",
    "don’t question me",
    "you’re not smart enough to understand this",
    "you’ll never be able to do this without me",
    "everyone agrees with me",
    "this is the only way",
    "you’ll lose everything if you don’t listen",
    "don’t make me do something I’ll regret",
    "think about the consequences of your actions"
]

def detect_gaslighting_or_manipulation(sentence):
    """
    Analyze the input sentence to determine if it contains signs of gaslighting or manipulation.

    Parameters:
        sentence (str): The input sentence to analyze.

    Returns:
        dict: A report indicating whether gaslighting or manipulation was detected and the reasons why.
    """
    sentence_lower = sentence.lower()

    # Check for gaslighting patterns
    gaslighting_matches = [pattern for pattern in GASLIGHTING_PATTERNS if re.search(pattern, sentence_lower)]

    # Check for manipulation keywords
    manipulation_count = sum(keyword in sentence_lower for keyword in MANIPULATION_KEYWORDS)

    # Check for additional manipulative phrases
    manipulative_phrase_matches = [phrase for phrase in ADDITIONAL_MANIPULATIVE_PHRASES if phrase in sentence_lower]

    # Sentiment analysis using TextBlob
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)

    # Compile results
    report = {
        "gaslighting_detected": bool(gaslighting_matches),
        "manipulation_detected": manipulation_count > 0 or bool(manipulative_phrase_matches),
        "gaslighting_patterns": gaslighting_matches,
        "manipulation_keyword_count": manipulation_count,
        "manipulative_phrases": manipulative_phrase_matches,
        "sentiment_score": sentiment,
    }

    return report

# Example usage
if __name__ == "__main__":
    test_sentence = (
        "After everything I've done for you, you’re imagining things. You always overreact."
    )

    analysis_report = detect_gaslighting_or_manipulation(test_sentence)

    print("Gaslighting and Manipulation Detection Report:")
    for key, value in analysis_report.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
