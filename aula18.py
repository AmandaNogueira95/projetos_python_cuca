#CALCULAR IMC
#SOLICITA PESO E ALTURA E APLICA O CALCULO DE ACORDO COM A TABELA DE INFORMAÇÕES DE IMC
#APOS IMPRIMIR AS INFORMAÇÕES SOBRE PESO, ALTURA, VALOR CALCULADO DO IMC, VAI MOSTRAR A SITUAÇÃO SE ENCONTRA O VALOR CALCULADO

print("------------------------ CALCULADORA DE IMC --------------------------------")

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

print("\nAltura: ",altura)
print("Peso: ",peso)
print("IMC: ",imc)

if imc < 16.9:
    print("Situação: Muito abaixo do peso")
elif imc <= 18.4:
    print("Situação: Abaixo do peso")
elif imc <= 24.9:
    print("Situação: Peso normal")
elif imc <= 29.9:
    print("Situação: Acima do peso")
elif imc <= 34.9:
    print("Situação: Obesidade Grau I")
elif imc <= 40:
    print("Situação: Obesidade Grau II")
else:
    print("Situação: Obesidade Grau III")