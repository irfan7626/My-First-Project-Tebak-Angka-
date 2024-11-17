import random


def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Tebak angka dari angka 1 sampai {x}: " ))
        if guess < random_number:
            print("Maaf tebak lagi, angka terlalu kecil")
        elif guess > random_number:
            print("Maaf tebak lagi, angka terlalu besar")
    print(f"Yey benar, angkanya adalah {random_number}")



guess(10)
