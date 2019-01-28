x=int(input('enter the no   '))
q=x//100
r=x%100
r1=r%10
r2=r1%10 
q1=r//10
z=q**3+q1**3+r2**3
if   x==z:
     print('armstrong no')
else:
     print('not a armstrong no')      
