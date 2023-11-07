n1=float(input('digite o preço do produto 1: '))
n2=float(input('digite o preço do produto 2: '))
n3=float(input('digite o preço do produto 3: '))
if n1 < n2 < n3 or n1 < n3 < n2 :
    print('O produto que você deve comprar é o 1, com um preço de {} R$ '.format(n1))
elif n2 < n1 < n3 or n2 < n3 < n1:
    print('O produto que você deve comprar é o 2, com um preço de {} R$'.format(n2))    
else:
    print('O produto que você deve comprar é o 3, com um preço de {} R$'.format(n3))    

