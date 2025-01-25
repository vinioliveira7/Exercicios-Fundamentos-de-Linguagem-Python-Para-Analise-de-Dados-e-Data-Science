import re
from hangman_game_functions import choose_word, input_letter, clear_cmd, display_hangman, menu, choose_category
PATH = "hangman game/words.json"

def game():
    clear_cmd()

    print("\nBem-vindo(a) ao jogo da forca!")

    menu(PATH)

    category = choose_category(PATH)

    remaining_attempts = 6
    wrong_letters = []
    try:    
        word = choose_word(PATH, category)
    except FileNotFoundError:
        print("O arquivo das palavras não foi encontrado")
        return
    except ValueError:
        print("O arquivo é inválido")
        return
    
    print("Adivinhe a palavra abaixo: ")

    print(display_hangman(remaining_attempts))

    discovered_letters = (['_' if letter.isalpha() else letter for letter in word])
    print("Palavra: " + " ".join(discovered_letters)) 


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
  
        print(display_hangman(remaining_attempts))

        print("Palavra: " + " ".join(discovered_letters)) 

        if "_" not in discovered_letters:
            print(f"\nVocê venceu! A palavra era: {word}")
            break
    
    if "_" in discovered_letters:
        print(f"\nVocê Perdeu! A palavra era: {word}")


if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        clear_cmd()
        print("\nUsuário forçou a interrupção")        