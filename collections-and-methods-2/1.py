
def summ(n):
    if n == 1:
        return 1
    elif n%2 != 0:
        return n + summ(n-1)
    else:
        return summ(n-1)


print(summ(8))
