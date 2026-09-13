import random

# roll = random.randint(1, 6)
# print(f"You rolled a {roll}!")
# Peki bunu birçok kez yapmak istesek?

def roll_dice():
# Fonksiyonu tanımladık.
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!")

def throw_dice():
    roll_dice()
    roll_dice()
    # Fonksiyonu çağırdık, hem de başka fonksiyonun içerisinde.

def announce_coffe_run():
    print()
    print("I am headed to the coffee shop! Who wants latte?")
    print()

def calculate_total_cost(latte_quantity: int):
    print()
    print(f"{latte_quantity} lattes comes to ${latte_quantity * 5}.")
    print()

def you_are_welcome():
    print()
    print("You're welcome!")
    print("You're welcome!")
    print()

def coffee_run():
    announce_coffe_run()
    you_are_welcome()
    you_are_welcome()
    you_are_welcome()
    calculate_total_cost(0)

coffee_run()

def greet(name, unread_messages):
    print(f"Welcome, {name}! You have {unread_messages} new messages.")

greet("Sude", 15)

def sum(number1, number2):
    print(f"{number1} + {number2} = {number1 + number2}")

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters)
    print(scrambled_word)

scramble("mustafa")

def room_area(length, width):
    return length * width

area = room_area(12, 10)
print(f"The room is {area} square feet.")

def add_tax(price):
    return price * 1.08

total = add_tax(50)
print(f"With tax, that comes to ${total: .2f}.")

def full_name(first, last):
    return first + " " + last

name = full_name("Mustafa", "TAVASLI")
print(f"Welcome, {name}!")