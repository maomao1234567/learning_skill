import sys


class Test:
    def __init__(self, value='Hello Word!'):
        self.data = value

    def __repr__(self):
        return f'value: {self.data}'

    def __str__(self):
        return f'data: {self.data}'


if __name__ == '__main__':
    t = Test()
    print(t)
