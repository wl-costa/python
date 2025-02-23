#É possível converter o valor de um tipo para outro tipo utilizando os construtores
preco = 10 
preco = float(preco)
print(preco) 
# >>> 10.0

# Importante ressaltar que dividir um valor inteiro por outro valor resultará em um valor do tipo float
numero_inteiro = 10
resultado_divisao = numero_inteiro / 2
print(resultado_divisao)
# >>> 5.0

# Agora convertemos o resultado da divisao para o tipo inteiro
print(int(resultado_divisao))

# Entretanto, uma forma de preservar o valor inteiro no resultado de uma divisão é utilizar duas barras (//)
resultado_divisao_inteiro = numero_inteiro // 2
print(resultado_divisao_inteiro)

print("")

# Exemplos diversos
print(int(1.97348728)) #float para int
print(int("10")) #string para int
print(float("10.11")) #string para float
print(float(100)) #int para float

#Checando os tipos
valor = 10
valor_str = (str(valor))

print(type(valor))
print(type(valor_str))
