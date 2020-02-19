import random
print "This game is for prediction"
print "You have to guess a number between 1 and 201"
print "Good Luck!!!!"
print "-----------------------------"
hidden_guess = random.randrange(1,201)
attempts = 0
my_value = 0
for attempt in range(5):
  my_value = int(raw_input("please enter your guess :"))
  print("you entered %d" %my_value)
  if hidden_guess == my_value:
    print "Correct guess!!!!"
    break
  else:
    if hidden_guess > my_value:
      print("Loser, too low....")
    else:
      print("Loser, too high...")
    attempts = attempts + 1
    print("You attempted %d times" %attempts)
print("Game Over!, the correct answer is %d" %hidden_guess)
if hidden_guess == my_value:
   print("You are a winner")
