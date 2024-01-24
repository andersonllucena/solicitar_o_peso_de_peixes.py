# Solicitar o peso de peixes
peso_peixes = float(input("Informe o peso de peixes (em quilos): "))

# Definir o limite estabelecido pelo regulamento
limite_peso = 50

# Calcular o excesso e a multa, se houver
if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    valor_multa_por_quilo = 4.00
    multa = excesso * valor_multa_por_quilo
else:
    excesso = 0
    multa = 0

# Exibir os resultados
print(f"Peso informado: {peso_peixes:.2f} kg")

if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a ser paga: R$ {multa:.2f}")
else:
    print("Não há excesso de peso. Nenhuma multa será aplicada.")