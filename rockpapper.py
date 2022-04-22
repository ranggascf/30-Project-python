import random
from secrets import choice

print("Guntin Batu Kertas")
print("==================")

print("1.Gunting")
print("2.Batu")
print("3.Kertas")
print("==================")

tipe = input("Silahkan pilih : ")

if tipe in ("Gunting", "Batu", "Kertas"):
    choice = ("Gunting", "Batu", "Kertas")
    bot_random = random.choice(choice)
    print(tipe, "Lawan", bot_random)
    print("==================")

    #logikanya
    if tipe == bot_random:
        print("Seri")
    else:
        if tipe == 'Batu':
            if bot_random == 'Gunting':
                print("Menang")
            if bot_random == 'Kertas':
                print("Kalah")

        if tipe == 'Gunting':
            if bot_random == 'Batu':
                print("Menang")
            if bot_random == 'Kertas':
                print("Kalah")

        if tipe == 'Kertas':
            if bot_random == 'Gunting':
                print("Menang")
            if bot_random == 'Batu':
                print("Kalah")