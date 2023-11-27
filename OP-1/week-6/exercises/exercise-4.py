"""
Write a function that takes a sentence as input and counts the frequency of each word
in the sentence using a dictionary. Ignore punctuation and treat words in a case-insensitive
manner. Return a dictionary where keys are words and values are their frequencies.
"""

# Declare variables
sentence = "This is a sample text and it is a good sample"
sentence_low = sentence.lower()
list_words = sentence_low.split()
print(list_words)
# Declare function
def word_frequency(sentence):
    word_count = {}
    for word in list_words:
        if word in word_count:
            word_count[word] += 1
            print(word_count)
        else:
            word_count[word] = 1
            print(word_count)
    return word_count

# Call function
print(word_frequency(sentence))