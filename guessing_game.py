import random
import time
GoalNumber = int(random.randrange(1, 10))
for x in range(4):
  answer = int(input(   "I have chosen a number between 1 and 10. Can you guess it? Place your answer here: "  ))
  print(".")
  time.sleep(1)
  print(".")
  print("Game.bot is thinking...")
  time.sleep(1)
  print(".")
  print(".")
  time.sleep(1)
  if answer == GoalNumber:
    print("You found the number!")
    break

  if answer > GoalNumber:
    print("Your number is greater than the answer")
    print(" ")

  if answer < GoalNumber:
    print("Your number is less than the answer.")
    print(" ")
if answer != GoalNumber:
  print(
    f"Sorry, you ran out of guesses! The answer was {GoalNumber}"
  )

