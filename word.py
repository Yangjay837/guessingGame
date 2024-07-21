import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]


word = random.choice(words)


word_length = len(word)
trials = 5

print(f"Welcome to the word guessing game! The word has {word_length} letters.")
print("These words are names of Fruits")
print("You have 5 trials to guess the word.")

while trials > 0:
    
    guess = input("Enter your guess: ")

    
    if len(guess) != word_length:
        print("No, the word has", word_length, "letters.")
    else:
        
        if guess == word:
            print("Yes! Congratulations, you guessed the word!")
            break
        else:
            print("No")

    
    trials -= 1
    print(f"You have {trials} trials left.")

if trials == 0:
    print(f"Sorry, you didn't guess the word. The correct answer was {word}.")