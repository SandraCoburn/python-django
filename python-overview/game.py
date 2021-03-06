###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3]

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

#get guess
def get_guess():
  return list(input("What is your guess?"))
#generate computer code 123
def generate_code():
  digits = [str(num) for num in range(10)]
   #shuffle the digits
  random.shuffle(digits)
  #grab the first three
  return digits[:3]

#generate the clues
def generate_clues(code,user_guess):
  if user_guess == code:
    return "code cracked"
  clues = []
  for ind,num in enumerate(user_guess):
    if num == code[ind]:
      clues.append("match")
    elif num in code:
      clues.append("Close")
  if clues == []:
    return "Nope"
  else: 
    return clues

#run game logic
print("Welcome Code Breaker")
secret_code = generate_code()
print("Code has been generated, pless guess a 3 digit number")
#Empty Clue Report to start with
clue_report = []

#Keep asking until the user gets it right
while clue_report != "code cracked":
  #ask for guess
  guess = get_guess()
  #Give clues
  clue_report = generate_clues(guess, secret_code)
  print("here is the result of your guess:")
  for clue in clue_report:
    print(clue)

