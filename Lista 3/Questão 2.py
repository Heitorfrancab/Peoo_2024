# Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o primeiro nome da pessoa.
nome = input("Informe seu nome completo. ")

pnome = nome.split(" ")

print(f"Bem vindo ao Python, {pnome[0]}.")