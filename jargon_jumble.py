import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ___ meeting lasts until lunch."),
    ("syntax", "The rules of a programming language are called its ___."),
    ("bandwidth", "The amount of data that can be transmitted in a fixed amount of time is called ___."),
    ("deadline", "A ___ is a date or time by which something must be completed."),
    ("algorithm", "A step-by-step procedure for solving a problem or performing a task is called an ___."),
]

print("-" * 40)
print()
print("     Welcome to Jargon Jumble!")
print("     A Tech-Themed Word Scramble Game")
print()
print("-" * 40)

used = []
score = 0

round = 1
while round <= 3:
    word, hint = random.choice(word_bank)

    while (word, hint) in used:
        word, hint = random.choice(word_bank)

    used.append((word, hint))

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters).lower()

    print()
    print(f"Round: {round}")
    print(f"Scrambled Word: {scrambled_word}")
    print()

    user_selection = input("Guess the word (or type 'hint' / 'skip' / 'quit'): ").strip().lower()

    if user_selection == "hint":
        print()
        print("Hint:", hint)
        print()
        user_selection = input("Guess the word (or type 'skip'): ").strip().lower()
        # hint tercih edilirse tekrar kullanıcıdan cevap bekliyoruz.

    if user_selection == "quit":
        break
    elif user_selection == word:
        print("Congratulations! You guessed the word correctly.")
        score += 1
    elif user_selection == "skip":
        print("You skipped the word. The correct word was:", word)
    elif user_selection != word:
        print("Sorry, that's not the correct word. The correct word was:", word)
    else:
        print("Invalid input. Please try again.")

    round += 1

print(f"Final Score: {score}/{round}")

if score == round:
    print("Flawless! All tests passing, zero bugs.")