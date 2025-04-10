"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Požár
email: pozar@volny.cz
created: 10. 4. 2025
description:
             Skript spustí hru Bulls and Cows, ve které hráč hádá čtyřciferné číslo.
             Po každém pokusu je hráči sdělen počet bulls (správná číslice na správném místě)
             a cows (správná číslice na špatném místě). Hra pokračuje až do uhodnutí čísla.
"""

import random
import time
from typing import List, Tuple

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
def generate_random_number() -> List[int]:
    """
    Generuje náhodné 4místné číslo, které nezačíná nulou a nemá duplicitní číslice.
    
    Returns:
        List[int]: Seznam 4 číslic (int) představujících náhodné číslo
    """
     # Nejprve vytvoříme náhodný seznam 4 unikátních číslic z rozsahu 0-9
    random_number = random.sample(range(10), 4)    
    # Pokud první číslice je 0, vyměníme ji za jinou číslici
    if random_number[0] == 0:
        # Odstraníme nulu a vybereme novou číslici z ostatních (0-9 bez nulové pozice)
        random_number[0] = random.choice([digit for digit in random_number[1:] if digit != 0])
    return random_number  # Vrátí náhodné číslo jako seznam číslic
    
# Funkce pro získání platného tipu od uživatele
def get_guess() -> List[int]:
    """
    Získá od uživatele platný tip (4-ciferné číslo bez nul na začátku a bez duplicitních číslic).
    
    Returns:
        List[int]: Seznam 4 číslic (int) představujících tip uživatele.
    """
    while True:
        guess = input("Enter a number:\n" + "-" * 47 + "\n>>> ")
        
        # Kontrola, zda vstup obsahuje pouze 4 unikátní číslice a začíná jinou číslicí než 0
        if guess.isdigit() and len(set(guess)) == 4 and guess[0] != '0':
            return [int(digit) for digit in guess]  # Převede vstup na seznam číslic
        else:
            print("Invalid input! Please enter a 4-digit number that does not start with 0.",
                  "and contains no duplicate digits.")


# Funkce na porovnání dvou čísel
def compare_numbers(random_number: List[int], guess: List[int]) -> Tuple[int, int]:
    """
    Porovná náhodné číslo s tipem uživatele a vrátí počet bulls a cows.
    
    Args:
        random_number (List[int]): Seznam 4 číslic představujících náhodné číslo.
        guess (List[int]): Seznam 4 číslic představujících tip uživatele.
    
    Returns:
        Tuple[int, int]: Počet bulls (správné číslice na správném místě)
                          a cows (správné číslice na špatném místě).
    """
    bulls = cows = 0
    for i in range(4):
        if guess[i] == random_number[i]:  # Správné číslo na správném místě
            bulls += 1
        elif guess[i] in random_number:  # Správné číslo na špatném místě
            cows += 1
    return bulls, cows

# Hlavní funkce pro spuštění hry
def play_game() -> None:
    """
    Hlavní smyčka hry Bulls and Cows. Hráč hádá náhodné číslo a dostává zpětnou vazbu
    o počtu bulls a cows, dokud neuhodne správné číslo.
    """

    random_number = generate_random_number()  # Generování náhodného čísla
    start_time = time.time()  # Uložení času začátku hry
    tip_count = 0  # Počítadlo tipů

    while True:    
        guess = get_guess()  # Získání tipu od uživatele
        tip_count += 1  # Zvyšuje počet tipů o 1
        bulls, cows = compare_numbers(random_number, guess)  # Porovnání čísel

        # Výpis počtu bulls a cows s ohledem na jednotné/množné číslo
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == 4:
            end_time = time.time()  # Konec měření času
            elapsed_time = end_time - start_time  # Výpočet trvání
            print(f"Congratulations! You've guessed the right number\n"
                  f"in {tip_count} guesses!")
            print(f"Your time is: {elapsed_time:.2f} seconds")

            try:
                # Uložení výsledků do souboru
                with open("results.txt", "a") as file:
                    file.write(f"Time: {elapsed_time:.2f} seconds | Guesses: {tip_count}\n")
            except IOError as e:
                print(f"Chyba při zápisu do souboru: {e}")

            break  # Ukončení cyklu po správném uhádnutí

# Tento blok se spustí pouze pokud je soubor spuštěn přímo
if __name__ == "__main__":
    play_game()