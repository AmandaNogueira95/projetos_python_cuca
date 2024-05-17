print("------------------------------- PROGRAMA DE DOAÇÃO ---------------------------------------")
print("Opções para doar:")
print("Digite [01] Para Doar R$ 10,00")
print("Digite [02] Para Doar R$ 20,00")
print("Digite [03] Para Doar R$ 30,00")
print("Digite [04] Para Doar R$ 40,00")
print("Digite [05] Para Doar R$ 50,00")

opcao_doacao = input("Digite o número da opção desejada: ")

if opcao_doacao == "01":
    print("Você escolheu doar R$ 10,00. Obrigado pela sua doação!")
elif opcao_doacao == "02":
    print("Você escolhei doar R$ 20,00. Obrigado pela sua doação!")
elif opcao_doacao == "03":
    print("Você escolhei doar R$ 30,00. Obrigado pela sua doação!")
elif opcao_doacao == "04":
    print("Você escolheu doar R$ 40,00. Obrigado pela sua doação!")
elif opcao_doacao == "05":
    print("Você escolheu doar R$ 50,00. Obrigado pela sua doação!")
else:
    print("Opção inválida! Escolha uma opção válida de 01 a 05.")