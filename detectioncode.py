# Import necessary libraries
import nltk
from textblob import TextBlob
from collections import Counter

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_repetition(text):
    """
    Analyze the text for repetition or redundancy.
    Returns a score indicating the level of repetition.
    """
    words = nltk.word_tokenize(text)
    word_counts = Counter(words)
    repeated_words = sum(count > 1 for count in word_counts.values())
    repetition_score = repeated_words / len(word_counts)
    return repetition_score

def analyze_grammar(text):
    """
    Analyze the text for perfect grammar and syntax.
    Returns a score indicating the level of grammatical correctness.
    """
    blob = TextBlob(text)
    grammar_score = blob.correct().raw == text
    return grammar_score

def analyze_word_choice(text):
    """
    Analyze the text for unusual word choice.
    Returns a score indicating the level of unusual word choice.
    """
    blob = TextBlob(text)
    tagged_words = blob.tags
    unusual_words = [word for word, pos in tagged_words if pos == 'NNP' or pos == 'FW']
    unusual_word_score = len(unusual_words) / len(tagged_words)
    return unusual_word_score

def is_ai_generated(text):
    """
    Determine if the text is AI-generated or human-generated based on the analysis.
    Returns a boolean indicating if the text is likely AI-generated.
    """
    repetition_score = analyze_repetition(text)
    grammar_score = analyze_grammar(text)
    word_choice_score = analyze_word_choice(text)
    
    # Define thresholds for each trait
    repetition_threshold = 0.1
    grammar_threshold = 1.0
    word_choice_threshold = 0.2
    
    # Determine if the text is AI-generated based on the scores
    if (repetition_score > repetition_threshold and
        grammar_score == grammar_threshold and
        word_choice_score > word_choice_threshold):
        return True
    else:
        return False

# Example usage
text_entry = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
if is_ai_generated(text_entry):
    print("The text is likely AI-generated.")
else:
    print("The text is likely human-generated.")
