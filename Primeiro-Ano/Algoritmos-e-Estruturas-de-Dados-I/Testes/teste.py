import unidecode
import re
import nltk
import np

file = open('Aulas/newtp1.txt', 'r')
str2 = file.read()
vocabs = str2.split()
print(vocabs)

file2 = open('Aulas/tp1ex2.txt' 'r')
str3 = file2.read()
low_str2 = str3.lower()
no_accent2 = unidecode.unidecode(low_str2)
no_accent2 = re.sub(r',', '', no_accent2)
words = no_accent2.split()
sort_words = sorted(set(words))
print(sort_words)

sentence_vectors = []
for word in sort_words:
  word_token = nltk.word_tokenize(word)
  vector = []
  for vocab in vocabs:
    if vocab in word_token:
      vector.append(1)
    if vocab not in word_token:
      vector.append(0)

sentence_vectors.append(vector)
sentence_vectors = np.assaray(sentence_vectors)

print(sentence_vectors)
