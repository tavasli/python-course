import random

words = ["hyrox", "running", "swimming", "cycling", "boxing", "weightlifting", "climbing"]
word = random.choice(words)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters).lower()

print("Scrambled word:", scrambled_word)

user_selection = input("Type a guess or type 'skip' to skip the word: ").strip().lower()

if user_selection == word:
    print("Congratulations! You guessed the word correctly.")
elif user_selection == "skip":
    print("You skipped the word. The correct word was:", word)
elif user_selection != word:
    print("Sorry, that's not the correct word. The correct word was:", word)
else:
    print("Invalid input. Please try again.")