#Projeto 1
#Crie um programa que pergunte a nota do aluno e diga se ele passou:
#Nota >=6 e presenca acima de 75%

nota_1 = float(input("Qual a sua do primeiro bimestre ?"))
nota_2 = float(input("Qual a sua do segundo bimestre ?"))
nota_3 = float(input("Qual a sua do terceiro bimestre ?"))
nota_4 = float(input("Qual a sua do quarto bimestre ?"))
porcentagem_presenca = int(input("Qual a sua porcentagem de presenca?"))
media = (nota_1 + nota_2 + nota_3 + nota_4)/4
#Float em vez de int, float permite numero quebrado int nao

if media >= 6 and porcentagem_presenca >= 75:
        print("passou de ano")
else:
        print("reprovou de ano")
