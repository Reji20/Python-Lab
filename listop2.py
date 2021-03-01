from listop.Listop import *
l=input('Enter a list :')
new=l.split()
new=[int(i)for i in new]
print(new)
print('List with unique elements :')
unique(new)
print('List with square of elements :')
square(new)
