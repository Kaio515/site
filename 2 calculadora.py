#desejo fazer uma calculadora que seje capaz de utilizar todos os operadores ariritimetricos
while True:

    operador = input("Qual operacao voce deseja realizar? ")
    num_1 = float(input("Digite um numero? "))
    num_2 = float(input("Digite outro numero? "))

    if operador == "+":
        print(num_1 + num_2)

    elif operador == "-":
        print(num_1 - num_2)

    elif operador == "*":
        print(num_1 * num_2)

    elif operador == "/":
        print(num_1 / num_2)

    elif operador == "%":
        print(num_1 % num_2)

    elif operador == "**":
        print(num_1 ** num_2)

    else:
        print("operacao invalida")

    erro = input("Deseja tentar novamente? (S/N) ")

    if erro == "n" or erro == "N":
        print("espero ter ajudado")
        break