# Os operadores de associação são operadores utilizados para verificar se um objeto está presente em uma sequência
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)
# >>> True

print("maçã" not in frutas)
# >>> True

print(200 in saques)
# >>> False