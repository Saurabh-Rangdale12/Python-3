# Lambda Or Anonymous function

def add(a,b):
    return a+b

plus = lambda a,b:a+b

print(add(8,3))
print(plus(8,3))

a = [[1, 34], [8,12], [4, 89]]
a.sort(key= lambda x:x[1]) # lambda x:x[1] gives element at index 1 of x e.g 1,34 return 34
print(a)
