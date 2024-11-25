import copy
def main():
    l = [10,20,30,40,50]
    print(l[2])
    print(l[2:4]) # [2:3[
    print(l[-1])
    print(l[2:])
    print(l[:3])
    print(l[:])
    
    # s = "toto"
    # s[0] = "T"
    l[0] = 1000
    print(l)
    
    l1 = l.copy()
    # l1 = l[:]
    # l1 = copy.copy(l)
    l1 = l
    l[0] = 12
    print(l) # 12,...
    print(l1)
    
    a = 2
    print(50*'-')

    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
    l1 = l[:] # marche pas (shallow)
    l1 = l.copy() # marche pas (shallow)
    l1 = copy.deepcopy(l) # Marche ! 

    l[0][0] = 1000
    print(l)
    print(l1)
    
if __name__=='__main__':
    main()
