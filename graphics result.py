from graphics import rectangle as r
print('*********Rectangle*********\n')
a=int(input('Enter length:'))
b=int(input('Enter breadth:'))
print('area=',r.RectArea(a,b))
print('Perimeter=',r.RectPeri(a,b))

from graphics import circle as c
print('\n*********Circle*********\n')
r=int(input('Enter radius:'))
print('area=',c.CircleArea(r))
print('Circumference=',c.CirclePeri(r))

from graphics.dgraphics import cuboid as cu
print('\n*********Cuboid********\n')
l=int(input('Enter length:'))
b=int(input('Enter breadth:'))
h=int(input('Enter height:'))
print('area=',cu.CuboidArea(l,b,h))
print('Perimeter=',cu.CuboidPeri(l,b,h))

from graphics.dgraphics.sphere import *
print('\n*********Sphere*********\n')
r=int(input('Enter radius:'))
print('area=',SphereArea(r))
print('Circumference=',SpherePeri(r))
