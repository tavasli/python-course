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
