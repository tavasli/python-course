guests = ["Marcus", "Lena", "Sarah", "Priya"]

for guest in guests:
    print(f"Welcome, {guest}!")

nominees = ["PixelPal", "TaskTanic", "SnackMap", "MoodTunes"]

for nominee in nominees:
    print(f"Nominated for Best New App: {nominee}")

print("And those are your nominees!")

friends = [("Marcus", "Lasagna"), ("Lena", "Salad"), ("Sarah", "Brownies")]

for friend in friends:
    name, dish = friend
    print(f"{name} is bringing {dish}.")

lineup = [
    ("The Waiters", "reggae", 45),
    ("Daft Punk", "electronic", 90),
    ("Adele", "pop", 60),
    ("Metallica", "metal", 100),
]

for act in lineup:
    band, genre, minutes = act

    if minutes >= 90:
        print(f"{band} ({genre}) plays a long set: {minutes} minutes.")
    else:
        print(f"{band} ({genre}) plays {minutes} minutes.")

contacts = ["Freda", "Homer", "Chance"]

for index, contact in enumerate(contacts):
    print(index, contact)

def remove_contacts(contacts, name):
    for contact in contacts:
        if contact == name:
            contacts.remove(contact)
            print(f"Removed {name}.")
            return
            # Boş bir return atmazsak çalışmaya devam edecek.
    print(f"{name} isn't in your contacts.")

remove_contacts(contacts, "Mustafa")
remove_contacts(contacts, "Homer")

tasks = ["email Sam", "book the venue", "pay the band"]
first = tasks.pop(0)
# Hem çıkarır hem de değeri döner. remove() ile farkı buradadır.
tasks.insert(0, "pay rent")
# Belirli index konumuna ekleme yapmayı sağlar.

age = 24
if age >= 21:
    print("This person can ride.")

got_enough_sun = True
was_watered = True

if got_enough_sun and was_watered:
    print("It bloomed!")

is_costume_party = False
knows_nobody = True

if is_costume_party or knows_nobody:
    print("Hat's going on.")

is_weekend = False

if not is_weekend:
    print("Cat wins.")

orders = ["latte", "muffin"]

def serve_order(orders):
    if len(orders) == 0:
        print("Nothing left to serve.")
        return
    item = orders.pop(0)
    print(f"Seving: {item}")

serve_order([])

waitlist = []

def call_next(waitlist):
    """ Seat the first guest on the waitlist. """
    if len(waitlist) == 0:
        print("The waitlist is empty.")
        return
    name = waitlist[0]
    print(f"Now seating: {name}")

try:
    number = int("banana")
except ValueError:
    print("Please enter a number.")
# Hata oluşabilecek durumları doğru yönetmeyi sağlar.

try:
    number_of_hot_dogs = int(input("How many hot dogs can you eat? "))
    print(f"Signed up for {number_of_hot_dogs} hot dogs. Good luck!")
except ValueError:
    print("I need a number to sign you up.")