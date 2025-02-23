# Exibe uma linha de entrada do usuário e recebe uma entrada do mesmo e, após isso, atribui à variável nome
nome = input("infome o seu nome:")
sobrenome = input("informe o seu sobrenome:")
genero = "Masculino"

# Formas de se utlizar a função print
print(nome, sobrenome) # exibe as variáveis separando-os usando espaço
print(nome, sobrenome, end="...\n") # exibe as variáveis e adiciona uma quebra de linha
print(nome, sobrenome, genero, sep="#") # coloca um separador entre as variáveis