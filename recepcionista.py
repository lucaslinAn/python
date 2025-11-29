registro = []

for i in range (3):
     produto = str(input("Digite o nome do produto: "))
     qtde = int(input("Digite a quantidade de itens:"))
     valor = float(input("Digite o valor do produto:"))
     print("-----------------------------")

     registro = {
         "Produto": produto,
         "Quantidade": qtde,
         "Valor" : valor

     }
     registro.appende(registro)
     print("\n--- Lista de Registros ---")
     for i, r in enumerate(registro,start=1 ):
         print(f"{i}.Produto:{r["Produto"]}, Quantidade: {r["Quantidade"]}, Valor: {r["Valor"]}")