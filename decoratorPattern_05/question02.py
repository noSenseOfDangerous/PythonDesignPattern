condition=False
def withpara(para=True):
    def inner(fn):
        if para ==False:
            return fn

        def wrap_in(*args):
            print('inner start')
            fn(*args)
            print('inner end')

        return wrap_in

    return inner

@withpara(condition)
def f(a):
    return a+2

if __name__=='__main__':
    print(f(5))