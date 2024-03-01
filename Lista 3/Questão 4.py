# Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores podem ser números reais. Mostrar o resultado com duas casas decimais.
Base = int(input("Qual a base do retângulo? "))
Altura = int(input("Qual a altura do retângulo? "))

area = Base * Altura
perimetro = 2*Base + 2*Altura
diagonal = (Base**2 + Altura**2)**0.5

print(f"A área é: {area}; \nO perímetro é: {perimetro}; \nA diagonal é: {diagonal:.2f}.")