def pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(sentence.lower())
if __name__ == "__main__":
    test_sentence = "The quick brown fox jumps over the lazy dog"
    print(pangram(test_sentence))  # Output: True`
    test_sentence = "Hello World"
    print(pangram(test_sentence))  # Output: False
    test_sentence = "We promptly judged antique ivory buckles for the next prize"
    print(pangram(test_sentence))  # Output: True