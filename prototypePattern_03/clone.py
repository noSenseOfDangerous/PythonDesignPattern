import copy


class A:
    def __init__(self):
        self.x = 18
        self.msg = 'Hello'


class B():
    def __init__(self):
        self.A = A()
        self.y = 34

    def __str__(self):
        return '{}, {}, {}'.format(self.A.x, self.A.msg, self.y)


if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    print([str(i) for i in (b, c)])
    print([(i, i.A) for i in (b, c)])
#Output:
# ['18, Hello, 34', '18, Hello, 34']
# [(<__main__.B object at 0x7f0dc45c0710>, <__main__.A object at 0x7f0dc45f9588>), (<__main__.B object at 0x7f0dc465efd0>, <__main__.A object at 0x7f0dc45f9588>)]
