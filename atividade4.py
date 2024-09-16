nome=input('Qual seu nome? ')
n1=float(input('Nota do primeiro bimestre = '))
n2=float(input('Nota do segundo bimestre = '))
n3=float(input('Nota do terceiro bimestre = '))
n4=float(input('Nota do quarto bimestre = '))
s= n1+n2+n3+n4
m= s/4
print('A media do aluno,{} é {:.1f}'.format(nome,m))