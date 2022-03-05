

def generator(n):
    i = 0
    while i < n:
        i += 1
        if i%2 == 0:
        	yield i

for el in generator(200):
    print(f"{el/3:.2f}" if el%5 == 0 else el)
    