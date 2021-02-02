from graphics import rectangle as r
print('*********Rectangle*********\n')
a=int(input('Enter length:'))
b=int(input('Enter breadth:'))
print('area=',r.RectArea(a,b))
print('Perimeter=',r.RectPeri(a,b))

from graphics import circle as c
print('\n*********Circle*********\n')
a=int(input('Enter radius:'))
print('area=',c.CircleArea(a))
print('Circumference=',c.CirclePeri(a))

from graphics.dgraphics import cuboid as cu
print('\n*********Cuboid********\n')
a=int(input('Enter length:'))
b=int(input('Enter breadth:'))
c=int(input('Enter height:'))
print('area=',cu.CuboidArea(a,b,c))
print('Perimeter=',cu.CuboidPeri(a,b,c))

from graphics.dgraphics.sphere import *
print('\n*********Sphere*********\n')
a=int(input('Enter radius:'))
print('area=',SphereArea(a))
print('Circumference=',SpherePeri(a))
