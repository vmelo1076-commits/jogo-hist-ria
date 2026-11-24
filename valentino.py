numeroUm = input("primeiro numero")
numerodois = input("segundo numero")
resposta = input("1 = +, 2 = -, 3 = /, 4 = x,")

if resposta == "1":
    print(int(numeroUm) + int(numerodois))

if resposta == "2":
    print(int(numeroUm) - int(numerodois))

if resposta == "3":
    print(int(numeroUm) / int(numerodois))

if resposta == "4":
    print(int(numeroUm) * int(numerodois))

