from collections import Counter, defaultdict
import string
import re

# Clean text to keep only letters
def clean_text(text):
    return ''.join(c.lower() for c in text if c in string.ascii_letters)

# Step 1: Letter frequency analysis
def letter_frequency(text):
    cleaned = clean_text(text)
    total = len(cleaned)
    counts = Counter(cleaned)
    print("\nLetter Frequency:\n")
    for letter in string.ascii_lowercase:
        freq = counts.get(letter, 0)
        percent = (freq / total) * 100 if total > 0 else 0
        print(f"{letter}: {freq} ({percent:.2f}%)")

# Step 2.5: Cipher word frequency and English word suggestions
def get_most_common_cipher_words(text, top_n=5):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

# Small English word bank grouped by word length
english_word_bank = {
    2: ['of', 'to', 'in', 'it', 'is', 'on', 'by', 'an'],
    3: ['the', 'and', 'for', 'are', 'you', 'but', 'not'],
    4: ['that', 'with', 'have', 'this', 'from', 'they'],
    5: ['there', 'their', 'which', 'would', 'other'],
    6: ['people', 'should', 'little', 'public', 'within'],
}

def suggest_possible_words(cipher_text, top_n=5):
    common_cipher_words = get_most_common_cipher_words(cipher_text, top_n)
    
    print("\n🔍 Most Frequent Cipher Words and Possible English Guesses:\n")
    for word, freq in common_cipher_words:
        length = len(word)
        possible = english_word_bank.get(length, [])
        guess_list = ', '.join(possible) if possible else 'No match found'
        print(f"'{word}' (length {length}, occurs {freq}×): Possible guesses → {guess_list}")

# Main program
cipher_text = input("Enter cipher text:\n")

letter_frequency(cipher_text)
suggest_possible_words(cipher_text)
