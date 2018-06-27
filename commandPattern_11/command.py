import os

verbose = True


class RenameFile:
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print('[renaming {} to {}]'.format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print('[renaming {} back to {}]'.format(self.dest, self.src))


def delete_file(path):
    if verbose:
        print('[deleting file "{}"]'.format(path))
    os.remove(path)


class CreateFile:
    def __init__(self, path, txt='file content'):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print('[Create file "{}"]'.format(self.path))
        with open(self.path, 'w') as f:
            f.write(self.txt)

    def undo(self):
        if verbose:
            print('[undo creating file "{}"]'.format(self.path))


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print('[Reading file "{}"]'.format(self.path))
        with open(self.path, 'r') as f:
            print(f.read())


def main():
    org_name, new_name = 'file1', 'file2'
    commands = []
    for cmd in CreateFile(org_name), ReadFile(org_name), RenameFile(org_name, new_name):
        commands.append(cmd)

    [c.execute() for c in commands]

    answer = input('reverse the excuted commands? [y/n]')

    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


if __name__ == '__main__':
    main()
