#AULA 15 - ESTRUTURA DE DECISÃO

#SOLICITAR O ANO ATUAL E O ANO DE NASCIMENTO E CALCULAR A IDADE DA PESSOA
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento
print("\nIdade: ", idade, "anos")
if idade >= 18:
    print("Status: Maior de idade")
else:
    print("Status: Menor de idade")