import re
from collections import Counter

def TextAnalyzer(text):

    word = re.findall(r'\b\w+\b', text.lower())
    sentence = re.split(r'[.!?]', text)
    sentence = [s.strip() for s in sentence if s.strip()]

    total_words = len(word)
    unique_word = len(set(word))
    total_sentences = len(sentence)
    avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0
    word_frequency = Counter(word)
    most_common_word = word_frequency.most_common(5)
    char_count = len(text)
    char_count_with_no_spaces = len(text.replace(" ", ""))

    return {
        "Total Words": total_words,
        "Unique Words": unique_word,
        "Total Sentences": total_sentences,
        "Average Sentence Length": avg_sentence_length,
        "Most Common Words": most_common_word,
        "Character Count": char_count,
        "Character Count (no spaces)": char_count_with_no_spaces
    }
