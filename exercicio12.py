s= float(input('digite o seu salario atual '))

if s<=280:
    percentual=20
elif s>=280<700:
    percentual=15
elif s>=700<1500:
       percentual=10
elif s>=1500:
       percentual=5
print('Salario antes do ajuste {}'.format(s))
percentual= percentual/100
aumento= percentual*s
s_novo= s+aumento
print('O percentual de aumento {} %'.format(percentual))
print('O valor do aumento {} R$'.format(aumento))
print('Seu salario novo {} R$'.format(s_novo))

   
       