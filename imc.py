print("Este é um teste avaliativo de IMC - segue as perguntas abaixo: ")
altura = float(input("Qaul é a sua altura? "))
peso = float(input("Qual é o seu peso? "))

IMC = peso / altura **2


print (IMC) 

if IMC <= 18.5:
    print("Voce está abaixo do peso. ")
elif IMC <= 24.9:
    print("Seu peso está ideal. ")
elif IMC <= 29.9:
    print("Sobrepeso. ")
elif IMC <= 34.9:
    print("Obesidade grau I. ")
elif IMC <= 39.9:
    print("Obesidade grau II. ")
else:
    print("Obesidade grau III. (mórbida) ")


