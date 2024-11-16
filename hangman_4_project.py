import random

# words = ["UMBRELLA", "COMPUTER", "TELESCOPE", "SMARTPHONE"]
f = open('words.txt', 'r')
# print(guessed_word)
data = f.readline()
words = data.split()
# print(words)
word = random.choice(words)
word = word.upper()
total_chances = 7
guessed_word = "-"*len(word)
while total_chances != 0:
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
                print(guessed_word)
        if guessed_word == word:
            print("Congratulation you won! ")
            break
    else:
        total_chances -= 1
        print("Incorrect guess")
        print("the remaining chances are: ", total_chances)
else:
    print("Game over")
    print("You lose")
    print("All chances are finish")
print("The correct word: ", word)
