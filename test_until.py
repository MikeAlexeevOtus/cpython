import dis


def x(n):
    until n == 0:
        str(n)      # check args passing (was a problem with symbol table)
        print(n)
        n -= 1


dis.dis(x)
print('test call:')
x(10)
