n1=float(input('digite um número: '))
n2=float(input('digite um número: '))
n3=float(input('digite um número: '))
if n1 >= n2 >= n3 or n1 >= n3 >= n2:
    print('o numero maior é {}'.format(n1))
elif n2 >= n1 >= n3 or n2 >= n3 >= n1:
    print(' o número maior é {}'.format(n2)) 
elif n3 >= n2 >= n1 or n3 >= n1 >= n2 :
    print('o número maior é {}'.format(n3))
if n1 <= n2 <= n3 or n1 <= n3 <= n2:
    print('o numero menor é {}'.format(n1))
elif n2 >= n1 <= n3 or n2 <= n3 <= n1:
    print(' o número menor é {}'.format(n2)) 
elif n3 <= n2 <= n1 or n3 <= n1 <= n2 :
    print('o número menor é {}'.format(n3))

