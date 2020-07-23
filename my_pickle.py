class JustCounter:
    _secrete_count = 0
    public_count = 0

    def __init__(self, count):
        self._secrete_count = count
        self.public_count = count

    def count(self):
        self.public_count += 1
        self._secrete_count += 1


class SubJustCounter(JustCounter):
    _secrete_count = 0
    public_count = 0

    def __init__(self, count):
        self._secrete_count = count
        self.public_count = count
        super(SubJustCounter, self).__init__(count)


class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def _get_name(self):
        return self._name


class Student(Person):

    def _get_name(self):
        return 'hello'


def outer():
    number = 10
    print(number)

    def inner():
        nonlocal number
        number = 20
        print(number)
    inner()
    print(number)


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


class A:
    pass


class B(A):
    pass


class C(B):
    pass


class Pe:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_name(cls, name, age):
        return cls(name, age)


if __name__ == '__main__':
    p = Pe('ym', 20)
    print(p)
    print(p.get_name('wxc', 18))
