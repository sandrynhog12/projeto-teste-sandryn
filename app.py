nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
possui_cnh = True
if idade <= 17:
    print('Vc é menor de idade! ')
elif idade >= 18 and possui_cnh == False :
    print('Vc apneas é de maior, porém, não possiu CNH! ') 
elif idade >= 18 and possui_cnh == True :
    print('Vc é de maior, e possiu CNH! ')        
else:
    print('Vc não pode Dirigir ')    