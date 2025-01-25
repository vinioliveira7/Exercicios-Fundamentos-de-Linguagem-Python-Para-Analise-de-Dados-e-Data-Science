import re
from hangman_game_functions import choose_word, input_letter, clear_cmd
PATH = "hangman game/words.json"

def game():
    clear_cmd()

    remaining_attempts = 6
    wrong_letters = []
    word = choose_word(PATH, "frutas")

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    discovered_letters = (["_" for letter in word])
    print(" ".join(discovered_letters))


    while remaining_attempts > 0:
        print(f"\nTentativas restantes: {remaining_attempts}")
        print("Letras erradas:", " ".join(wrong_letters))
 
        letter_attempt = input_letter()

        if letter_attempt in word:
            index = 0
            for letter in word:
                if letter_attempt == letter:
                    discovered_letters[index] = letter
                index += 1
        else:
            remaining_attempts -= 1
            wrong_letters.append(letter_attempt)

        print(" ".join(discovered_letters))

        if "_" not in discovered_letters:
            print(f"\nVocê venceu! A palavra era: {word}")
            break
    
    if "_" in discovered_letters:
        print(f"\nVocê Perdeu! A palavra era: {word}")


if __name__ == "__main__":
    game()

            

            
            