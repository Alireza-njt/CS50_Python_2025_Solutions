# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

class Jar:

    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity
        self.n = 0

    def __str__(self):
        cookie = '🍪'
        str = ''
        for _ in range(self.n):
            str += cookie
        return str

    def deposit(self, n):
        new_n = self.n + n
        if new_n > self._capacity:
            raise ValueError
        self.n = new_n

    def withdraw(self, n):
        new_n = self.n - n
        if new_n < 0:
            raise ValueError
        self.n = new_n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n


def main():
    my_jar = Jar()
    my_jar.deposit(10)
    print(str(my_jar))


if __name__ == '__main__':
    main()
