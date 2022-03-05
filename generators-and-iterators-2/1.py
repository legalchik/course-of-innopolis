

def generator(n):
    i = -1
    while i < n:
        i += 1
        yield i


for el in generator(250):
    print(el)
