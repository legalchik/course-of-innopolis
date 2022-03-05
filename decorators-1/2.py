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
def peri(a):
	time.sleep(1)
	return a**2


print(peri(750219084328953985239852897323897077580932))
