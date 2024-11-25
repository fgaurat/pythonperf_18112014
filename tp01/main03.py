import lib

def main():
    a= 2    
    global a
    print(lib.a)
    # a=3
    # if True:
    #     a=2
    print(a)

if __name__ == "__main__":
    print("avant",a)
    main()
    print("après",a)
