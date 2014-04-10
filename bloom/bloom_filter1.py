bloom = 0

# read in training words
file = open('training-words.txt', 'r')
for word in file:
  word = word.rstrip()
  length = len(word)
  key = 1 << length
  bloom = bloom | key

print 'Bloom: ' + bin(bloom)

file = open('test-words.txt', 'r')
for word in file:
  word = word.rstrip()
  length = len(word)
  key = 1 << length
  if (key | bloom) != bloom:
    print word + ' (' + bin(key) + ')' + ' not in set'
