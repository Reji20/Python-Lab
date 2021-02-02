

# NO:4 - Write example program to demonstrate Chained exception.

try:
    
    try:
        a = int(input('Enter a integer : '))
        if a<0:
            print('Found negative')
    except ValueError as ve:
        print('Inner Block: ',ve)
        raise IOError('Keyboard Error') from ValueError
except ValueError as ve:
    print('Outer Block: ',ve)
except IOError as ie:
    print('Outer Block: Chained Error caught : ',ie)
        