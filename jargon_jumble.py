import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ___ meeting lasts until lunch."),
    ("syntax", "The rules of a programming language are called its ___."),
    ("bandwidth", "The amount of data that can be transmitted in a fixed amount of time is called ___."),
    ("deadline", "A ___ is a date or time by which something must be completed."),
    ("algorithm", "A step-by-step procedure for solving a problem or performing a task is called an ___."),
]

word, hint = random.choice(word_bank)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters).lower()

user_selection = input("Guess the word (or type 'hint' / 'skip'): ").strip().lower()

if user_selection == "hint":
    print()
    print("Hint:", hint)
    print()
    user_selection = input("Guess the word (or type 'skip'): ").strip().lower()
    # hint tercih edilirse tekrar kullanıcıdan cevap bekliyoruz.

if user_selection == word:
    print("Congratulations! You guessed the word correctly.")
elif user_selection == "skip":
    print("You skipped the word. The correct word was:", word)
elif user_selection != word:
    print("Sorry, that's not the correct word. The correct word was:", word)
else:
    print("Invalid input. Please try again.")