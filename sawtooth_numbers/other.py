from operator import lt, gt


def is_sawtooth(n):
    ns = str(n)
    for i in range(1, len(ns)):
        if not [gt, lt][i % 2](ns[i - 1], ns[i]):
            return False
    return True


L = int(input('L = '))
R = int(input('R = '))
print(len([x for x in range(L, R + 1) if is_sawtooth(x)]))
