
# RESULTAOD DE FATORIAIS

numero = int(input("Fatorial de: ") )
if numero > 0: #MAIOR QUE 0 = N° INT
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item    
print(fatorial)
