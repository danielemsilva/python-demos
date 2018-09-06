# Remove repeated characters from a word
def remove_repeat(word):
  new_word = ''
  if len(word) != 0:
    new_word = word[0]

  for i in range(len(word)):
    if word[i] != new_word[-1]:
      new_word += word[i]

  return new_word

word = raw_input("Enter a word:")
print "Result:", remove_repeat(word)
