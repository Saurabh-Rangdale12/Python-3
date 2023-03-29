a = 9
b = 8
# c = sum((a,b)) # buit in function
# print(c)

def function1(): #  like this we define function in python
    print("Hello you are in function1", a+b)

function1()
function1()
function1()
def fun2(a, b):
    print("Hello you are in fun2", a+b)
fun2(5, 7)
fun2(15, 7)
fun2(5, 9)

def fun3(a, b):
    """This doc String and we can print it."""
    return (a + b)/2
avg = fun3(7, 19)
print(avg)

print("doc String: ", fun3. __doc__) # This is how we print doc of function

