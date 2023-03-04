def make_keeper(n):
    def a(f):
        c = 1
        while c<=n:
            if f(c):
                print(c)
            c += 1
    return a


def is_even(x):
        return x % 2 == 0
make_keeper(5)(is_even)
        