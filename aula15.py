#EMPRESA REGISTRA PRODUTOS
#CONTROLE DE ESTOQUE
#SOLICITAR QUANTIDADE DOS 4 PRODUTOS
#SOMAR A QUANTIDADE DOS PRODUTOS
#IF SE A QUANTIDADE TOTAL DO ESTOQUE TIVER MENOR QUE 100, DE 10 PARA CIMA ESTOQUE NORMAL

print("----------------- CONTROLE DE ESTOQUE ----------------------")
prodA = int(input("Digite a quantidade de produtos A: "))
prodB = int(input("Digite a quantidade de produtos B: "))
prodC = int(input("Digite a quantidade de produtos C: "))
prodD = int(input("Digite a quantidade de produtos D: "))
total_estoque = prodA + prodB + prodC + prodD

print("\nEstoque atual: ",total_estoque)
if total_estoque < 100:
    print("ATENÇÃO, ESTOQUE EM BAIXA QUANTIDADE!!!")
else:
    print("Estoque Normal :D")