from abc import ABCMeta, abstractmethod


class SensitiveInfo(metaclass=ABCMeta):
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print("There are {} users: {}".format(len(self.users), ' '.join(self.users)))

    @abstractmethod
    def add(self, user):
        self.users.append(user)
        print("Added user {}".format(user))


class Info(SensitiveInfo):
    def __init__(self):
        self.secret = '0xdeadbeef'
        super().__init__()

    def read(self):
        super().read()

    def add(self, user):
        sec = input('What is the secret?')
        super().add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username:')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))


if __name__ == '__main__':
    main()
