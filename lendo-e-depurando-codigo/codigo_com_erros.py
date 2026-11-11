# Simulador de compra de supermercado

produto = "Arroz"
preco_unitario = 5.79
quantidade = 3

# Cálculo do valor total
valor_total = preco_unitário * quantidade

#Aplicando desconto de 10% se a quantidade for maior que 2
se quantidade > 2:
    valor_total = valor_total * 0,9

print("Produto:", produto)
print("Quantidade comprada:", quantidade)
print("Valor total da compra: R$", + valor_total)
