import os

os.system("clear")
# Write a program that prints the longest sentence in a string based on the number of words. You should also print the number of words in the longest sentence.

# Sentences may end with periods (.), exclamation points (!), or question marks (?). You should treat any sequence of characters that are not spaces or sentence-ending characters as a word. Thus, -- should count as a word. Log the longest sentence and its word count. Pay attention to the expected output, and be sure you preserve the punctuation from the end of the sentence.

# Note that this problem is about manipulating and processing strings. As such, every detail about the string matters (e.g., case, punctuation, tabs, spaces, etc.).


def find_word_count(sentence: str):
    return len(sentence.split())


def longest_sentence(text: str):
    punctuation = (".", "!", "?")
    sentences = []
    current_sentence = ""
    for char in text:
        current_sentence += char
        if char in punctuation:
            sentences.append(current_sentence)
            current_sentence = ""

    if current_sentence:
        sentences.append(current_sentence)

    sentences.sort(key=find_word_count, reverse=True)
    long_sentence = sentences[0]
    long_sent_wc = find_word_count(long_sentence)
    print()
    print(f"{long_sentence}\n")
    print(f"The longest sentence has {long_sent_wc} words.")
