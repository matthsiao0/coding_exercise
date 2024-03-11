def f():
    yield {
        '$id': {
            1: 0
        }
    }
    yield {
        2: 10
    }

g = f()
print(list(g))
# print(next(g))