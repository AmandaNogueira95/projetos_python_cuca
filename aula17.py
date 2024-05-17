#DESENVOLVER UM PROGRAMA PARA CALCULAR O VALOR A SER DESCONTADO DE INSS DE ACORDO COM O SALARIO. 
#O PROGRAMA DEVE COLETAR INFORMAÇÃO DO VALOR DO SALARIO E FAZER A COMPARAÇÃO DO SEU VALOR DE ACORDO COM A TABELA DE INSS 2024
#EXTRAIR A ALIQUOTA E USAR ELA PARA CALCULAR O VALOR A SER DESCONTADO
#AO FINAL DEVE IMPRIMIR O RESULTADO DE | VALOR DO SALARIO | ALIQUOTA DE DESCONTO | VALOR DESCONTADO | SALARIO LIQUIDO

print("--------------------------------------- DESCONTO DE INSS ----------------------------------------")
salario = float(input("Qual o seu salário atual?: "))

if salario <= 1412:
    aliquota = 7.5
    desconto = salario * (aliquota / 100)
elif salario <= 2666:
    aliquota = 9
    desconto = salario * (aliquota / 100)
elif salario <= 4000:
    aliquota = 12
    desconto = salario * (aliquota / 100)
elif salario <= 7786:
    aliquota = 14
    desconto = salario * (aliquota / 100)
else:
    aliquota = 0
    desconto = 0

salario_liquido = salario - desconto

print("\nValor do salário: R$",salario)
print("Aliquota de INSS aplicada: ",aliquota)
print("Valor do desconto de INSS: R$",desconto)
print("Valor líquido a receber: R$",salario_liquido)
    