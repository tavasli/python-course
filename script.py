import random
# Module ekledik.

skills = ["Git", "Python", "Swift"]
years = [5, 0, 4]
about_me = ["🏊🏼", "🛫", "👨🏻‍💻"]
print("Skills:", skills)
print("Years of Experience:", years)
print("About Me:", about_me)

tickets = ["Ada", "Grace", "Linus", "Margaret", "Alan"]
now_helping = tickets[0]
next_in_line = tickets[1]
just_added = tickets[-1]
# Negatif indeksleme sondan başlayarak gelir.
print()
print("Now helping: ", now_helping)
print("Next in line: ", next_in_line)
print("Just added: ", just_added)

first_match = ["earth", "heart"]
second_match = ["below", "elbow"]
third_match = ["night", "tight"]

word1 = list(first_match[0])
word2 = list(first_match[1])
word3 = list(second_match[0])
word4 = list(second_match[1])
word5 = list(third_match[0])
word6 = list(third_match[1])

print(f"{first_match[0]} and {first_match[1]} are anagrams." if sorted(word1) == sorted(word2) else f"{first_match[0]} and {first_match[1]} are not anagrams.")
print(f"{second_match[0]} and {second_match[1]} are anagrams." if sorted(word3) == sorted(word4) else f"{second_match[0]} and {second_match[1]} are not anagrams.")
print(f"{third_match[0]} and {third_match[1]} are anagrams." if sorted(word5) == sorted(word6) else f"{third_match[0]} and {third_match[1]} are not anagrams.")

players = ["Mara", "Devon", "Priya", "Leo"]
random.shuffle(players)
print(players)
random_player = random.choice(players)
print(f"{random_player} deals first.")

letters = ["p", "y", "t", "h", "o", "n"]
print("/".join(["mysite.com", "products", "sale"]))
print("-".join(["2026", "04", "30"]))
print(" ".join(["hip", "hip", "hurray"]))
print("".join(letters))

promo_code = "FLASH50"
user_code = input("Enter your promo code: ")
print("Promo code is valid!" if user_code == promo_code else "Invalid promo code.")

unread_messages = 0
age = 25
cart_total = 45
tickets_left = 8
print(f"Has unread messages (more than 0): {unread_messages > 0}")
print(f"Old enough to rent a car (25 or older): {age >= 25}")
print(f"Under the $50 free shipping minimum: {cart_total < 50}")
print(f"Sold out (0 tickets left): {tickets_left == 0}")

student_score = int(input("Enter your score: "))
if student_score >= 60:
    print("Congratulations! You passed the test.")
else:
    print("Sorry, you did not pass the test. Better luck next time.")

signal = 2
if signal == 0:
    print("%50 off, sorry about the Wi-Fi!")
elif 1 <= signal <= 2:
    print("%25 off.")
elif 3 <= signal <= 4:
    print("%10 off.")
elif signal == 5:
    print("Full bars, no discount today!")

code = "spring26"
full_name = "jamie rivera"
email = "  Jamie@Example.COM"
display_name = "   the ROCK   "
print(code.upper())
print(full_name.title())
print(email.lower().strip())
print(display_name.strip().title())