#coding : utf-8
class LazyProperty:
    def __init__(self,method):
        self.method=method
        self.method_name=method.__name__

    def __get__(self, instance, owner):
        if not instance:
            return  None
        value=self.method(instance)
        #print(('value {}'.format(value)))
        setattr(instance,self.method_name,value)
        return value

class Test:
    def __init__(self):
        self.x='foo'
        self.y='bar'
        self._resouce=None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resouce))
        self._resouce=tuple(range(5))  # 代价大的
        return self._resouce

def main():
    t=Test()
    print(t.x)
    print(t.y)
    # 做更多的事情。。。
    print(t.resource)
    print(t.resource)

if __name__ == '__main__':
    main()