#AULA 13 - ATIVIDADE PRÁTICA - INPUT E ESTRUTURA DE DECISÃO

#SOLICITAR O NOME E AS NOTAS
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 01: "))
nota2 = float(input("Digite a nota 02: "))
nota3 = float(input("Digite a nota 03: "))
nota4 = float(input("Digite a nota 04: "))

#CALCULAR A MÉDIA
media = (nota1 + nota2 + nota3 + nota4) / 4

#MOSTRAR AS NOTAS E MÉDIA

print("-------------------- BOLETIM ESCOLAR --------------------")
print("\nNome do aluno: ", nome_aluno)
print("Nota 01: ", nota1)
print("Nota 02: ", nota2)
print("Nota 03: ", nota3)
print("Nota 04: ", nota4)
print("Média: ", media)

#VERIFICAR SE ALUNO FOI APROVADO OU REPROVADO
if media >= 7.0:
    print("Situação: Aluno Aprovado")
else:
    print("Situação: Aluno Reprovado")