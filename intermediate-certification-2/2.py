import time


def timing(function):
    def wrapped(*args):
        start = time.perf_counter()
        res = function(*args)
        stop = time.perf_counter() - start
        print(f"[Fuction finished in {stop:.8f}s]")
        return res
    return wrapped

@timing
def ss(a, b):
	time.sleep(1)
	return a*b

print(ss(12, 12))
