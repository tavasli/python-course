my_party = 2
print(my_party)

my_party += 2
print(my_party)

food_total = 100
drinks_total = 15
meal_total = food_total + drinks_total
print(meal_total)
# drinks_total -= 5
# Güncelleme olsa da meal_total değişkeni etkilenmez. O yüzden direkt gidip değiştirelim.
print(meal_total)

morning = "Drink coffee"
afternoon = "Skiing"
evening = "Watching a movie"
plan_for_today = "My plan for today is: 1. " + morning + " 2. " + afternoon + " 3. " + evening
print(plan_for_today)

first_name = "Metin"
event = "football match"
number = 2
noun = "meetings"
verb = "attend"
excuse = f"Sorry {first_name}, I can't come to the {event} because I have a {number} {noun} to {verb}."
# f-string ile direkt değeri alabiliyoruz.
print(excuse)

songs_in_my_library = 200
songs_in_my_library -= 47
print(f"I have {songs_in_my_library} songs in my library.")

ticket_cost = 12
number_of_tickets = 3
print(f"The total cost for {number_of_tickets} tickets is ${ticket_cost * number_of_tickets}.")

numbers_of_stickers = 48
number_of_friends = 6
stickers_per_friend = numbers_of_stickers / number_of_friends
print(f"Each friend will get {stickers_per_friend} stickers.")

hourly_rate = float(input("What's your hourly rate? "))
hours_worked = int(input("How many hours did you work? "))
print(type(hourly_rate))
print(type(hours_worked))
total_pay = hourly_rate * hours_worked
print(f"Your total pay is ${total_pay}.")
