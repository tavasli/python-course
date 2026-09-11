import random

words = ["HYROX", "BOXING", "RUNNING", "CYCLING", "SWIMMING"]
selected_word = random.choice(words)
letters = list(selected_word)
random.shuffle(letters)
# Burada zaten karıştırıyor, tekrar yapmaya çalışma.
scrambled_word = "".join(letters)

print(scrambled_word)