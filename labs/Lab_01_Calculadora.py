def sum(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

operations = {1: "Soma", 2: "Subtração", 3: "Multiplicação", 4: "Divisão"}

print("********** Calculadora Python **********\n")

while True:

    for k, v in operations.items():
        print(f"{k} - {v}")

    choice = int(input("\nEscolha o número da sua operação: "))
    if choice not in operations.keys():
        print("\nNão existe operação com esse número, tente novamente.\n")
        continue
    number1 = float(input("\nEscolha seu primeiro número: "))
    number2 = float(input("\nEscolha seu segundo número: "))

    if choice == 1:
        print(f"\n{number1} + {number2} = {sum(number1, number2)}")
        break
    elif choice == 2:
        print(f"\n{number1} - {number2} = {subtraction(number1, number2)}")
        break
    elif choice == 3:
        print(f"\n{number1} * {number2} = {multiplication(number1, number2)}")
        break
    elif choice == 4:
        if number2 == 0:
            print("\nNão é possível realizar divisão por zero")
        print(f"{number1} / {number2} = {division(number1, number2)}")
        break
        
