# Laço For que retorna as vogais contidas em um texto, percorrendo todas as letras do texto
# e verificando se a letra é uma vogal, caso seja, a letra é impressa na tela
# O método end="" é utilizado para evitar a quebra de linha após a impressão de cada letra

# Exemplo utilizando um iterável (string) para percorrer as vogais contidas em um texto

texto = str(input("Digite um texto: "))
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
print()

# Incrementado o valor de um número em 1, utilizando o laço for
# O laço for é utilizado para repetir a operação de incremento do número
numero = int(input("Digite um número: "))

for i in range(1):
    numero += 1
else: #else é opcional, utilizado para executar um bloco de código após o término do laço
    print(numero)
    
# range(1) é utilizado para definir a quantidade de vezes que o laço
# for será executado, neste caso, o laço for será executado 1 vez

# Exemplo do range(start, stop, step) com a tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end=" ")
    
    
# Exmeplo usando o while

opcao = -1

while opcao != 0:
    opcao = int(input("\n [1]Sacar \n [2]Depositar \n [0]Sair \n Escolha uma opção: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Depositando...") 
    else:
        print("Opção inválida. Tente novamente.")

print("Sistema encerrado.")

# O laço while é utilizado para repetir um bloco de código enquanto a condição
# definida for verdadeira, neste caso, o laço while será repetido até que a opção seja igual a 0

# Exemplo de uso do break

while True:
    numero = int(input("Digite um número: "))
    if numero == 10:
        break
    
    print(numero)
    
# No exemplo acima, o laço while será repetido até que o número digitado seja igual a 10
# Quando o número digitado for igual a 10, o break é executado, encerrando o laço while
    
# Exemplo de uso do continue com o laço for para imprimir os números ímpares de 0 a 100
    for i in range(100):
        if i % 2 == 0:
            continue
        print(i, end=" ")

# O continue é utilizado para pular a execução do bloco de código e continuar a execução do laço for
# Neste caso, o continue é utilizado para pular a impressão dos números pares e continuar a impressão dos números ímpares