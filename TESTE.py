nomes = []
clientes = int(input("Digite quantos clientes antendemos: "))

for i in range(clientes):
    nome = input("Digite o nome: "). capitalize()
    nomes.append(nome)

print("\nOs clientes do dia foram: \n")

for nome in nomes:
    print(nome)