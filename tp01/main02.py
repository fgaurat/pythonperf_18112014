import sys


if __name__ == "__main__":
    a = 2
    print(hex(id(a)))
    a = 3
    print(hex(id(a)))
    b=3
    print(hex(id(b)))
    print(a)
    print("------")
    print(sys.getrefcount(54678913334566))
    d = 54678913334566  
    print(sys.getrefcount(54678913334566))
    e = 54678913334566  
    print(sys.getrefcount(54678913334566))