sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.lower().split()

word_count = {word: words.count(word) for word in words}

print(word_count)
