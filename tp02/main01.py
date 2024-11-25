

def make_incrementor(i): # 10

    def the_function(j): # 2
        return i+j
    
    return the_function


def main():
    do_inc = make_incrementor(10)
    r = do_inc(2)
    print(r) # 12
    r = do_inc(52)
    print(r) # 12
    r = do_inc(32)
    print(r) # 12

if __name__=='__main__':
    main()
