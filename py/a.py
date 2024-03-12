import json

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

def a():
    print('function a')

def b():
    print('function b')
a = {'a': a, 'b': b}

a['a']()
a['b']()

print(b'{"name": "hello"}'.decode('utf-8'))
print(type(b'{"name": "hello"}'.decode('utf-8')))
j = json.loads(b'{"name": "hello"}'.decode('utf-8'))
print(j)
print(type(j))
print(json.loads(b'{"name": "hello"}'.decode('utf-8')))