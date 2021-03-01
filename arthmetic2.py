import arthmetic.add as a
from arthmetic import sub as s
from arthmetic.Arthmetic.mul import mul
from arthmetic.Arthmetic.div import *
x=int(input('Enter first number :'))
y=int(input('Enter second number :'))
print('SUM =',a.add(x,y))
print('DIFFERENCE =',s.sub(x,y))
print('PRODUCT =',mul(x,y))
print('QUOTIENT =',div(x,y))

