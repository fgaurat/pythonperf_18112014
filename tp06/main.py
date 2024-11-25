from Rectangle import Rectangle

class Test:

    def __new__(cls):
        print("def __new__(cls)")
        return object.__new__(cls)

    def __init__(self):
        print("def __init__(self)")

    def __call__(self):
        print("__call__(self)")

def main():
    t = Test()
    t()
    print(50*'-')
    r = Rectangle(2,3)
    r1 = Rectangle(25,38)

    print(hex(id(r)))
    print(hex(id(r1)))

    print(type(r))
    print(type(Rectangle))

if __name__=='__main__':
    main()
