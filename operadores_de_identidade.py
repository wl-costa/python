# Os operadores de identidade são operadores que, resumidamente, checam se dois objetos testados ocupam a mesma posição na memória
curso = "Curso de Python"
nome_curso = curso

saldo, limite = 200, 200

print(curso is nome_curso)
# >>> True

print(curso is not nome_curso)
# >>> False

print(saldo is limite)
# >>> True