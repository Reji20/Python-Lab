def zero_exception():
    try:
        a=5
        b=0
        print(a/b)
    except (ZeroDivisionError,ValueError) as e:
        print('dividing by zero')
    finally:
        print('finally block excecuted')
zero_exception()

