sentence="Count the number of words in sentences !"

def count_words(sentence):
   words=sentence.split()
   return len(words)

print(count_words(sentence))