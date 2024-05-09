print('CALCULADORA')
print('+ Adicao')
print('- Subtracao')
print('* Multiplicacao')
print('/ Divisao')
print('Pressione qualquer outra tecla para sair. ')

op = input('Qual operacao deseja realizar?')
x = int(input ('Digite o primeiro valor: '))
y = int(input ('Digite o segundo valor: '))

if op == '+':
    res = x + y
    print(f'resultado: {x} + {y} = {res}')
elif op == '-':
     res = x - y
     print(f'resultado: {x} - {y} = {res}')
elif op == '*':
     res = x * y
     print(f'resultado: {x} x {y} = {res}')
elif op == '/':
     res = x / y
     print(f'resultado: {x} / {y} = {res}')
else:
     print('Encerrando o programa...')