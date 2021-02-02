a=int(input('enter a number :'))
try:
    if a<90 or a>120:
        raise ValueError('Abnormal Condition')
except ValueError as ve:
    print(ve)
else:
    print(a,'is within 90 and 120')