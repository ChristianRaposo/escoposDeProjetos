print('================================CALCULADORA DE CONSUMO DE ENERGIA=============================================')

watts = float(input(f'Insira a potência do seu dispositivo em Watts: '))
horas = float(input(f'Insira em o tempo de consumo em horas: '))
dias = int(input(f'Por quantos dias você usa o dispositivo no mês? '))

eq1 = (watts * horas * dias) / 1000
eq2 = (eq1 * 0.73363)

print(f'O seu dispositivo consumiu {eq1}kWh durante o período informado')
print(f'E teve um impacto de {eq2:.2f} R$ na sua conta de luz!')
