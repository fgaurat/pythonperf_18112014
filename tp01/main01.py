# import lib as l
from lib import hello as remote_hello


def hello():
    return "Toto"


if __name__ == "__main__":
    # r = l.hello()
    r = remote_hello()
    r1 = hello()
    print(r)
    print(r1)

