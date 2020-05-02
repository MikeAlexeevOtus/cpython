import dis


def test():
    val = 10
    print('before change:', val, 'id:', id(val))
    val--
    print('after decrement:', val, 'id:', id(val))
    val++
    print('after increment:', val, 'id:', id(val))


dis.dis(test)
print('test new operations')
test()
