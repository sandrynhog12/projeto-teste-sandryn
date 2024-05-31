nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
possui_cnh = False
if idade <= 17:
    print('Vc é menor de idade! ')
elif idade >= 18 and possui_cnh == False :
    print('Vc apneas é de maior, porém, não possiu CNH! ')     
else:
    print('Vc pode dirigir')    