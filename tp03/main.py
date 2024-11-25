import traceback

class DivBy12Error(Exception):

    def __init__(self):
        super().__init__("Hoooooooo! la division par 12")

def div(a,b):
    if b==12:
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    c=0
    try:
        print('OPEN FILE')
        c = div(a,b)
    finally:
        print('CLOSE FILE')
    
    return c


def main():
    try:
        a = 2
        # b = int(input("b:"))
        b = 12
        # c = a/b
        c = call_div(a,b)
        print(c)
    # except TypeError as e:
    #     print("TypeError",e)
    #     # traceback.print_exc()
    # except ZeroDivisionError as e:
    #     print("ZeroDivisionError",e)
    #     # traceback.print_exc()
    # except ValueError as e:
    #     print("ValueError",e)
    #     # traceback.print_exc()
    except Exception as e:
        print("Exception",e,type(e))
    else:
        print("pas d'erreur")
    
    print("la suite du code")


if __name__=='__main__':
    main()
