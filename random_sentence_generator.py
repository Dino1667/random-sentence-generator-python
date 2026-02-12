import random

names = ["Edi", "Maria", "John", "Anna", "Tom", "Sofia"]
verbs = ["eats", "drinks", "throws", "jumps over", "kicks"]
objects = ["pizza 🍕", "coffee ☕", "ball ⚽", "cake 🎂", "car 🚗"]
places = ["in the park", "at home", "at school", "on the street", "in the garden"]
adjectives = ["funny", "crazy", "huge", "tiny", "lazy"]

print("🎉 Random Sentence Generator 🎉\n")

while True:
    sentence = f"{random.choice(names)} {random.choice(verbs)} {random.choice(adjectives)} {random.choice(objects)} {random.choice(places)}."
    print(sentence)
    input("Click [Enter] to create a new one")

