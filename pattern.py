def A():
    al = str()
    n = 5
    tn = 3*n

    for i in range(2*n):
        if i == 5:
            al+= 5*'*'
            al += '\n'
        for j in range(i,n):
            al += ' '
        al += '*'
        for k in range(n,i+n):
            al += ' '
        al += '*\n'
    print(al)
    return al


def I():
    i = 0
    il = str()
    n = 5
    for i in range(2*n):
        for j in range(n):
            il += ' '
        il += '*\n'
    print(il)
    return il





    # for i in range(5):
    #     for j in range(i,n):
    #         al += ' '
    #     al += '*\n'
    
    # tmp = str()

    # for i in range(5):
    #     for z in range(5):
    #         tmp += ' '
    #     for j in range(0,i):
    #         tmp += ' '
    #     tmp += '*'
    #     for k in range(i,10):
    #         tmp += ' '
    #     tmp += '\n'

    # print(al)
    # print(tmp)


def M():
    al = str()
    n = 10
    for i in range(n):
        al+= '*'
        tmp = n//2

        for j in range(tmp):
            al += ' '


            al += ' '
        al += '*'


def H():
    al = str()
    n = 10
    for i in range(n):
        if i == 5:
            for z in range(n+2):
                al+= '*'
            al += '\n'
        else:
            al += '*'
            for j in range(n):
                al += ' '
            al += '*\n'

    print(al)


def N():
    n = 10
    al = str()
    for i in range(n):
        al += '*'
        

        for j in range(0,i):
            al += ' '
        al+= '*'
        for j in range(i,n):
            al += ' '
        al += '*\n'

        
    print(al)

def S():
    al = str()
    n = 10

    for i in range(n):
        al += '*'
    al += '\n'

    for i in range(n//2-1):
        al += '*\n'
    
    for i in range(n):
        al += '*'
    al += '\n'

    for j in range(n//2-1):
        for i in range(n-1):
            al += ' '
        al+= '*\n'

    for i in range(n):
        al += '*'
    al += '\n'

    print(al)

def U():
    al = str()

    n = 10;
    for i in range(n-1):
        al += '*'
        for j in range(n):
            al += ' '
        al+= '*\n'
    
    for i in range(n+2):
        al += '*'
    al += '\n'

    print(al)


def M():
    n = 10;
    al = str()

    for i in range(n+1):

        al += '*'
        m = n

        for j in range(m-i,m):
            al += ' '
        al += '*'

        for j in range(0,m-i):
            al += ' '

        for j in range(0,m-i):
            al+= ' '
        al += '*'

        for j in range(m-i,m):
            al+= ' '
        al += '*\n'
    
    print(al)
    

A()        
I()
H()
N()
S()
H()
U()
M()
# s = input("Enter your name\n")
# s.lower()
# ans = str()


# for c in s:
#     if c == 'a':
#         ans += A()
#         ans += "\t"



