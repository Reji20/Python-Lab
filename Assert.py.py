

# NO:4 - Write example program to re-raised exception and AssertError (self-study) in Python. 

try:
    
    try:
        a=int(input('Enter your age :'))
        if a>15:
            raise ValueError('Invalid number') 
    except ValueError as ve:
        print(ve)
        raise
    else:
        print('Valid number')
except AssertionError as ae:
    print(ae)
except ValueError as ve:
    print('re-rased exception',ve)