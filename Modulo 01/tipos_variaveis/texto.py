# Declaração
nome_completo = "Testando Nome Completo"
nome_completo_aspas = """Testando
Davi
Ruan
"""

nome_completo_quebra = "Gabriel \
Casemiro"

nome = "Teste"
sobrenome = "Dando Certo"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Casemiro" + "Testando")
print("Nome completo (4a forma):" + "Gabriel", "Casemiro")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma):{nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))

print("-----------------------------------")
# upper() deixa todas as letras em maiúsculas
nome = nome.upper()
print(nome)

print("-----------------------------------")
# lower() deixa todas as letras em minúsculas
nome = nome.lower()
print(nome)

print("-----------------------------------")
# Utiliza [] para pegar uma letra
nome = nome[0]
print(nome[0])
print("-----------------------------------")

# utilizar .count() para determinar quantas vezes aparece
nome_completo = nome_completo.count("a")

print(nome_completo, "letras")

print("-----------------------------------")

# utiliza .find() para determinar o índice
# print(nome_completo.find("a"))
