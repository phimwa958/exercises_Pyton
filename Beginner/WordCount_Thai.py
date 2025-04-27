import re
import pythainlp

# Function to count words in Thai text
def count_words(text):
    words = pythainlp.word_tokenize(text)  # ใช้ PyThaiNLP ในการตัดคำ
    return len(words)

# Function to count sentences in Thai text
def count_sentences(text):
    sentences = re.split(r'[.!?]|[ๆฯ]', text)  # แยกประโยคด้วยจุด เครื่องหมายตกใจ เครื่องหมายคำถาม ๆ หรือ ฯ
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

# Function to count characters in text (excluding spaces)
def count_characters(text):
    return len(text.replace(" ", ""))

# Function to count syllables in Thai text
def count_syllables(text):
    words = pythainlp.word_tokenize(text)  # ใช้ PyThaiNLP ในการตัดคำ
    syllables = 0
    for word in words:
        syllables += len(re.findall(r'[ก-ฮะ-ูเ-ไ]+', word))  # นับพยางค์โดยใช้กลุ่มสระในแต่ละคำ
    return syllables

# Get input text from the user
text = input("ป้อนข้อความภาษาไทย: ")

# Call functions to count words, sentences, characters, and syllables
word_count = count_words(text)
sentence_count = count_sentences(text)
character_count = count_characters(text)
syllable_count = count_syllables(text)

# Display counts
print(f"จำนวนคำ: {word_count}")
print(f"จำนวนประโยค: {sentence_count}")
print(f"จำนวนตัวอักษร (ไม่รวมช่องว่าง): {character_count}")
print(f"จำนวนพยางค์ (ประมาณ): {syllable_count}")
