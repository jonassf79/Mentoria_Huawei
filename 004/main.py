area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = area / 3
latas = (litros / 18)
precoTotal = latas * 80

print(f"Você precisará de {latas} latas de tinta")
print(f"O preço total é R$ {precoTotal:.2f}")
