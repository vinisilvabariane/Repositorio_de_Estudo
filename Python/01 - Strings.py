nome = 'Maria de Lurdes'
altura = 1.8
idade = 54
peso= 60
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos seu imc e:'
linha_3 = f'{imc}'

print(linha_1)
print(linha_2)
print(linha_3)

a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f}'.format(a,b,c)
print (formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

a = 'A'
b = 'B'
c = 1.40394032
formato = 'a={} b={} c={:.2f}'.format(
    nome1=a ,nome2=b ,nome3=c
)
print(formato)

