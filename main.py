import random

num = random.randint(1, 100)

while True:
    guess = int(input("Son top: "))

    if guess == num:
        print("Topding!")
        break
    elif guess < num:
        print("Katta")
    else:
        print("Kichik")
