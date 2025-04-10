import string

def reverse_string(s):
    """Return the reversed version of the string."""
    return s[::-1]

def capitalize_words(s):
    """Return the string with each word capitalized."""
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    """Return the string with all punctuation removed."""
    return s.translate(str.maketrans('', '', string.punctuation))
