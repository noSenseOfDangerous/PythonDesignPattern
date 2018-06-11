def outer(fn):
    def wrap_out(*args):
        print('outer start')
        fn(*args)
        print('outer end')
    return wrap_out


def inner(fn):
    def wrap_in(*args):
        print('inner start')
        fn(*args)
        print('inner end')

    return wrap_in

@outer
@inner
def f(a,b,c):
    print (a+b+c)

if __name__=='__main__':
    print(f(2,3,5))
