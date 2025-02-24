# Exemplo 1: Estrutura Condicional Simples
MAIOR_IDADE = 18
IDADE_MINIMA = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH.")
elif idade >= IDADE_MINIMA:
    print("Pode Iniciar as aulas práticas.")
else:
    print("Não pode tirar a CNH.")
