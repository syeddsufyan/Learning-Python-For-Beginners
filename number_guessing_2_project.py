# Run Jupyter Notebook

import random
comp_number = random.randrange(1,101)
user_input = int(input("Enter Your Guess Number"))

if user_input>comp_number:
	print("Computer Number", comp_number)
	print("Guess Number Too Heigh")
elif comp_number>user_input:
	print("Computer Number", comp_number)
	print("Guess Number Too Low")
else:
	print("Computer Number", comp_number)
	print("Your Guess Number Match")