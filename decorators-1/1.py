

def decorator(foo):
    def wrapped(music):
        return foo(music) + ' ♫'
    return wrapped

@decorator
def function(music):
    return music

print(function('Dura - gotova'))
