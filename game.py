import random

name = input("Enter your name: ")
print(f"Welcome {name}. Hope you have a fun time.")
print("Welcome to the fruits edition.")
print("Let's begin")
print("------------------ START ---------------")

words = ["strawberry", "apple", "pineapple", "watermelon", "guava", "mango", "banana", "dragonfruit", "passionfruit", "grapes", "orange","lemon", "lychee", "muskmelon", "apricot", "berry", "papaya", "peach", "coconut" ]
word = random.choice(words)

guesses = ""
rounds = len(word) + 1
while(rounds):
    failed = 0
    print(f"########### Total rounds : {rounds} #####################")
      

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed+=1
    if (failed==0):
        print(" \n CONGRATULATIONS!!")
        print("You guessed it correct")
        print(f"The word was: {word}")
        print("Come back again.")
        break
    guess = input("\n Enter your guess: ")
    guesses += guess

    if guess not in word:
        print("Wrong")
        rounds-=1

        if rounds == 0:
            print("Rounds are over.")
            print("Try again next time!")
            break

