class checkEx(Exception):pass
try:
    a=input('enter a usernamem :')
    b=input('enter a passwords :')
    x='reji@001'
    y='5555'
    if a==x and b==y:
         print('valid login')
    else:
        raise checkEx('invalid login')
except checkEx as e:
    print(e)