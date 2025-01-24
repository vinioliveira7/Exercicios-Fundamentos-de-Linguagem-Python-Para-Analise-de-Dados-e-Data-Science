import json
import re
from random import randint, choice
from os import system, name

def clear_cmd():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def choose_word(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    chosen_list = data["frutas"]
    word = choice(chosen_list).lower()
    return word

def input_letter():
    while True:
        letter = input("\nDigite uma letra (a-z): ")
    
        if re.match("^[a-z]$", letter):
            return letter
        else:
            print("Entrada inválida. Apenas uma letra de 'a' a 'z' é permitida.")
            
