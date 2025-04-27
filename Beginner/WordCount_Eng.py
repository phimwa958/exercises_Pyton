import re

# Function to count words in text
def count_words(text):
    words = text.split()
    return len(words)

# Function to count sentences in text
def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)  # Split by '.', '!', or '?' followed by any whitespace
    # Remove empty strings from the list
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

# Function to count characters in text (excluding spaces)
def count_characters(text):
    return len(text.replace(" ", ""))

# Function to count syllables in text (simplified estimation)
def count_syllables(text):
    syllables = 0
    words = text.split()
    for word in words:
        syllables += len(re.findall(r'[aeiouyAEIOUY]+', word))  # Count vowel clusters as syllables
    return syllables

# Get input text from the user
text = input("Enter some text: ")

# Call functions to count words, sentences, characters, and syllables
word_count = count_words(text)
sentence_count = count_sentences(text)
character_count = count_characters(text)
syllable_count = count_syllables(text)

# Display counts
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")
print(f"Character count (excluding spaces): {character_count}")
print(f"Syllable count (estimated): {syllable_count}")
