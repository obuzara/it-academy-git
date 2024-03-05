def f(*args):
    return {v: k for k, v in args}


dct = {1: 'один', 2: 'два'}
print(dct)
print(f(*dct.items()))