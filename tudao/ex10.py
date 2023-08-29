numero = int(input('me diga um numero e eu digo a tabuada dele: '))

print(f"Tabuada do {numero}:")
tabuada = [numero * i for i in range(1, 11)]
for i, resultado in enumerate(tabuada, start=1):
    print(f"{numero} x {i} = {resultado}")
