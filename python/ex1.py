# Welcome to Hang Man / Problem #1.
# Required knowledge:
'''
split
join
len
random.choice
while
'''


import random

word_banks = [
    'shoulder','aluminium','portion','dominant','peasant','split','sandwich','employ','unfair','swarm','upset','possession','beneficiary','mosque','priority','contact','linen','tank','government','economic','mutual','mail','advertise','bedroom','rear','bloody','depart','outer','win','stomach','bond','dismiss','zero','meal','girlfriend','miscarriage','tread','spontaneous','unlawful','weigh','brush','contrast','exception','strikebreaker','primary','metal','determine','follow','graduate'
]

rand_word = random.choice(word_banks)
len_rand_word = len(rand_word)
guess_word = "__ " * len_rand_word
arr_guess_letter = guess_word.split(" ")
char_index = 0
lives = 5
answered = guess_word
continue_guess = True

print("Picked", rand_word)

while continue_guess:
   guess_letter = str(input(f"\nWord: {answered} \nGuess the letter: "))
   if guess_letter == rand_word[char_index]:
       arr_guess_letter[char_index] = guess_letter
       answered = " ".join(arr_guess_letter)
       char_index += 1
   else:
       lives -= 1
       print(f"\nRemaining live(s) {lives}")
   if lives <= 0:
       print("You lost! :[")
       continue_guess = False
       break
   if rand_word == "".join(answered.split(" ")):
       print("You got it! :]")
       break
  
