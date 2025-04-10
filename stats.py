def count_characters(s):
    """Return the number of characters in the string."""
    return len(s)

def count_words(s):
    """Return the number of words in the string."""
    return len(s.split())

def average_word_length(s):
    """Return the average word length in the string."""
    words = s.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)
