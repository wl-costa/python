def calcular_operacoes():
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))

    soma = x + y
    divisao = x / y if y != 0 else None #  else None significa que se y for zero, divisao recebe None (indicando que a operação não pode ser feita).
    multiplicacao = x * y

    return soma, divisao, multiplicacao

def obter_tipo():
    tipo = input("Você deseja o valor inteiro ou decimal? (Inteiro/Decimal) ").strip().lower()
    return tipo

def exibir_calculos():
    resultado = calcular_operacoes()
    tipo = obter_tipo()

    if tipo == "inteiro":
        soma = int(resultado[0])
        divisao = int(resultado[1]) if resultado[1] is not None else "Erro: divisão por zero"
        multiplicacao = int(resultado[2])
    elif tipo == "decimal":
        soma = float(resultado[0])
        divisao = float(resultado[1]) if resultado[1] is not None else "Erro: divisão por zero"
        multiplicacao = float(resultado[2])
    else:
        print("Opção inválida. Tente novamente.")
        exibir_calculos()
        return  # Sai da função para evitar repetição infinita

    print(f"Soma: {soma}, Divisão: {divisao}, Multiplicação: {multiplicacao}")

# Chamada principal
exibir_calculos()
