# Import necessary libraries
import nltk
from textblob import TextBlob
from collections import Counter

# Download necessary NLTK data files
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

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
text_entry1="Beneath the surface of the earth, where sunlight dared not tread, twelve-year-old Elias ventured into the heart of the crystal caverns, his lantern casting flickering shadows on walls that sparkled like a thousand frozen stars. The air was cool and damp, carrying the faint scent of minerals and ancient secrets. Around him, towering columns of amethyst and quartz rose like the bones of the earth itself, their jagged edges catching the light and scattering it into a kaleidoscope of colors. Elias’s heart raced with a mix of awe and trepidation as he ran his fingers along the smooth, glassy surface of a crystal, feeling the pulse of something ancient and alive beneath his touch. He had always been drawn to the unknown, to the places others feared to explore, but here, in the depths of the caverns, he couldn’t shake the feeling that the crystals were watching him, waiting for him to uncover the truth they had guarded for millennia."
text_entry2="The stars had been his companions for so long that their cold, distant light felt warmer than the sun that now scorched his weathered face. Captain Elias Voss sat on the jagged edge of the wreckage, his calloused fingers tracing the faded insignia on his tattered uniform. Four years. Four years since the *Astraeus* had plummeted into the uncharted dunes of this forsaken planet, leaving him stranded in a sea of silence. The ship’s carcass, half-buried in rust-colored sand, groaned in the wind, a mournful echo of the life he’d once known. His beard, streaked with gray, tangled like the vines that crept over the ruins of his home. He’d stopped counting the days after the first year, when hope had begun to feel like a cruel joke. Yet, even now, his eyes still scanned the horizon, not for rescue, but for something—anything—to remind him why he still clung to the fragile thread of survival. The stars, at least, hadn’t abandoned him. They whispered stories of the void, of the man he used to be, and of the man he might still become."
text_entry3="In a startling turn of events, Dr. Elena Martinez, a renowned research scientist at the Quantum Physics Institute, inadvertently created a microscopic black hole during a high-energy particle collision experiment. The incident, which occurred late Tuesday evening, has sent shockwaves through the scientific community. Initial reports suggest that the black hole, though minuscule, exhibited unexpected stability, raising concerns about its potential growth and the implications for Earth's safety. Emergency protocols were swiftly enacted, and the research facility has been placed under strict quarantine while international experts assess the situation. Dr. Martinez, visibly shaken, stated, \"This was never our intention. We were exploring the boundaries of quantum mechanics, but nature has reminded us of its unpredictable power.\" Authorities are urging calm as investigations continue, but the event has already sparked heated debates about the ethics and risks of advanced scientific experimentation."
text_entry4="Well, that is just what we see when one of our triangular or other acquaintances comes toward us in Flatland. As there is neither sun with us, nor any light of such a kind as to make shadows, we have none of the helps to the sight that you have in Spaceland. If our friend comes closer to us we see his line becomes larger; if he leaves us it becomes smaller: but still he looks like a straight line; be he a Triangle, Square, Pentagon, Hexagon, Circle, what you will - a straight Line he looks and nothing else. You may perhaps ask how under these disadvantageous circumstances we are able to distinguish our friends from one another: but the answer to this very natural question will be more fitly and easily given when I come to describe the inhabitants of Flatland. For the present let me defer this subject, and say a word or two about the climate and houses in our country."
text_entry5="Overhead, a huge storm was brewing, with clouds blacker than I’d ever seen over the city. I figured maybe it was global warming or something, because the weather all across New York State had been weird since Christmas. We’d had massive snow storms, flooding, wildfires, from lightning strikes, I wouldn’t have been surprised if this was a hurricane blowing in."
text_entry6="Multivac was self-adjusting and self-correcting. It had to be, for nothing human could adjust and correct it quickly enough or even adequately enough. So Adell and Lupov attended the monstrous giant only lightly and superficially, yet as well as any men could. They fed it data, adjusted questions to its needs and translated the answers that were issued. Certainly they, and all others like them, were fully entitled to share in the glory that was Multivac's."

text_entries = [text_entry1, text_entry2, text_entry3, text_entry4, text_entry5, text_entry6]

for text in text_entries:
    if is_ai_generated(text):
        print("The text is likely AI-generated.")
    else:
        print("The text is likely human-generated.")
