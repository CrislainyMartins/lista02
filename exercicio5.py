n1= float(input('Digite sua nota parcial:  '))
n2= float(input('Digite outra nota pacial: '))
media=(n1+n2)/2
if media==10:
    print('Aprovado com distinção') 
elif media>=7:
    print('Aprovado') 
else:
    print('Reprovado')       
