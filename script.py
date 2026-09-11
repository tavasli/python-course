import random

steel_blue = (70, 130, 180)
red, green, blue = steel_blue
# Her birine sırasıyla değerler atanır.

inventory = [
    ("notebooks", 42),
    ("pens", 130),
    ("staples", 8),
]

print(f"{inventory[0][0]}: {inventory[0][1]} in stock.")
print(f"{inventory[1][0]}: {inventory[1][1]} in stock.")
# İç içe şekilde index ile erişiyoruz.
item, quantity = inventory[2]
print(f"{item}: {quantity} in stock.")
# Burada da tuple çıkarıp değişkenlere atamayı kullandık.

count = 1
while count <= 5:
    if count == 3:
        break
    print(f"Count is: {count}")
    count += 1
    # Değişim olmalı ki sonsuz döngü olmasın.

PASSENGERS = 5
passenger_num = 1
while passenger_num <= PASSENGERS:
    print(f"Printing boarding pass {passenger_num} of {PASSENGERS}...")
    passenger_num += 1

lobby = []
lobby.append("Xena")
lobby.append("Thor")
lobby.append("Merlin")
lobby.append("Ripley")
print(lobby)

entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
winners = ["Diego", "Sofia"]

winner = random.choice(entrants)
while winner in winners:
    winner = random.choice(entrants)

winners.append(winner)
print(f"Newest Winner is {winner}")