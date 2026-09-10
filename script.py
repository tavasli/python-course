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