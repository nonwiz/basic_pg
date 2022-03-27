
word = input('Input a word:')
reversed_word = ''

for index in range(len(word), 0, -1):
    reversed_word += word[index-1]

print('Original word:', word, '| Reversed word:', reversed_word)