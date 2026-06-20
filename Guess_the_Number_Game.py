### IFEANYI EGENTI
name = input("Welcome player, Please enter your name: ")
print()

while name == "":
  print()
  print("You did not enter your name.")
  name = input("Please enter your name: ")

print()
print("Welcome to the Guess the Number game!", name)
print()
print(name, "I'm thinking of a number between 1 and 100. Can you guess my number?")
first_guess = int(input("guess my number: "))

import random
random_integer = random.randint(1,100)

while random_integer:
 if random_integer < first_guess:
  print("Unfortunately", name, "Your guess is too high. Please guess again.")
  first_guess = int(input("guess the number "))
 elif random_integer > first_guess:
  print("Unfortunately", name, "Your guess is too low. Please guess again.")
  first_guess = int(input("guess the number "))
 elif random_integer == first_guess:
  break

print()
print("Congratulations!!!", name,)
print("Your number:", random_integer, "is correct!")
print()
print("Thanks for playing!", name)

