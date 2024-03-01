#Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3). Considerar as notas com valores inteiros entre zero e cem.
nota1 = int(input("Informe a primeira nota. "))
nota2 = int(input("Informe a segunda nota. "))

media = (nota1*2 + nota2*3)//5

print(f"Sua média é {media}.")