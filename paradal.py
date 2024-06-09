
# velocidade = int(input('Velocidade Registrada? '))
# velo_permitida = 80
# if velocidade <= velo_permitida:
#     print('Não levou multa')
# elif velocidade > velo_permitida and velocidade <= velo_permitida +10:
#     print('Vc levou multa leve')     
# elif velocidade > velo_permitida + 11 and velocidade <= velo_permitida + 20:
#     print('Vc tomou multa grave ')    
# elif velocidade >  velo_permitida +20:
#     print('Sua multa foi gravíssima! ')    

def medidor_velo(velocida, velo_permitida):
    if velocida <= velo_permitida:
        print('Não levou multa')
    elif velocida > velo_permitida and velocida <= velo_permitida +10:
        print('Vc levou multa leve')     
    elif velocida > velo_permitida + 11 and velocida <= velo_permitida + 20:
        print('Vc tomou multa grave ')    
    elif velocida >  velo_permitida +20:
        print('Sua multa foi gravíssima! ')

medidor_velo(105,100)     