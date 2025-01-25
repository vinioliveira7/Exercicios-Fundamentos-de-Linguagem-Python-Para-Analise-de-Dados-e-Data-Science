import json
import re
from random import randint, choice
from os import name, system, path
PATH = "hangman game/words.json"

def clear_cmd():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def choose_word(archive_path, category):  
    with open(archive_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    chosen_list = data[category]
    word = choice(chosen_list).lower()
    return word
        
def input_letter():
    while True:
        letter = input("\nDigite uma letra (a-z): ")
    
        if re.match("^[a-z]$", letter):
            return letter
        else:
            print("Entrada inválida. Apenas uma letra de 'a' a 'z' é permitida.")

def display_hangman(chances):

    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]
            
def menu(archive_path):
    with open(archive_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    category_list = list(data.keys())
    for index in range(len(category_list)):
        print(f"{index+1} - {category_list[index].capitalize()}")

def choose_category(archive_path):
    with open(archive_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    category_list = list(data.keys())
    number_of_categories = len(category_list)

    while True:
        category = input("\nEscolha a categoria das palavras: ")

        if re.match("^[1-9]$", category) and int(category) <= number_of_categories: 
            return category_list[int(category)-1]
        else:
            print("Entrada inválida. Apenas um número é permitido")