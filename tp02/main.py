from functools import wraps


def do_log(log_file):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("Log before to",log_file,*args,**kwargs)
            r = func(*args,**kwargs)
            print("Log after to ",log_file,r)
            return r
        return wrapper
    return decorator


@do_log("the_log.log")
def say_hello(name):
    """
    Dit Bonjour !
    """
    
    s = f"Bonjour {name}"
    return s


def main():
    h = say_hello('Fred')
    print(h)
    print(say_hello.__name__)
    print(say_hello.__doc__)



if __name__=='__main__':
    main()
