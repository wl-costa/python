#Exemplo de declaração de variáveis
age = 23
name = 'Wendell'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = (24, 'Wendell')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

"""No Python não existem constantes, dependendo da convenção de Upper Case para
serem indentificadas"""

CPF = 80003768570
RG = 395693123
BIRTH_DATE = 13052001

# No Python uma das boas práticas é a de se utilizar o SNAKE_CASE
ABS_PATH = '/Desktop/PythonProjects/python'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.2