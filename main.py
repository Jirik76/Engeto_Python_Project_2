"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Požár
email:  pozar@volny.cz
"""

import random
import time

# Úvodní text
print(
    "*" * 48,
    "\n Hi there!",
    "\n" + "-" * 47,
    "\n I've generated a random 4-digit number for you.",
    "\n Let's play a Bulls and Cows game.",
    "\n" + "-" * 47,
    "\n",
    sep=""
)


# Generování náhodného 4místného čísla bez nuly na začátku
while True:
    random_number = random.sample(range(10), 4)
    if random_number[0] != 0:  # Zajistí, že číslo nezačíná 0
        break

# Funkce pro získání platného tipu od uživatele
def get_guess():
    while True:
       
        guess = input("Enter a number:\n" + "-" * 47 + "\n>>> ")
        
        # Kontrola, zda vstup obsahuje pouze číslice a začíná jinou číslicí než 0
        if guess.isdigit() and len(guess) == 4 and guess[0] != '0':
            return [int(digit) for digit in guess]  # Převede vstup na seznam číslic
        else:
            print("Invalid input! Please enter a 4-digit number that does not start with 0.")

# Funkce na porovnání dvou čísel
def compare_numbers(random_number, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == random_number[i]:  # Správné číslo na správném místě
            bulls += 1
        elif guess[i] in random_number:  # Správné číslo na špatném místě
            cows += 1
    return bulls, cows

# Hlavní smyčka hry

start_time = time.time() # Uložení času začátku hry
tip_count = 0 # Počítadlo tipů

while True:    
    
    guess = get_guess()
    tip_count += 1  # Zvyšuje počet tipů o 1
    bulls, cows = compare_numbers(random_number, guess)
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow")
    elif bulls == 1:
        print(f"{bulls} bull, {cows} cows")
    elif cows == 1:
        print(f"{bulls} bulls, {cows} cow")
    else:
        print(f"{bulls} bulls, {cows} cows")

    if bulls == 4:
        end_time = time.time()  # Konec měření času
        elapsed_time = end_time - start_time  # Výpočet trvání
        print(f"Congratulations! You've guessed the right number\n"
              f"in {tip_count} guesses!")
        print(f"Your time is: {elapsed_time:.2f} seconds")
        
        # Uložení výsledků do souboru
        with open("results.txt", "a") as file:
            file.write(f"Time: {elapsed_time:.2f} seconds | \
                         Guesses: {tip_count}\n")
        break
