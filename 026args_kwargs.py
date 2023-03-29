def fun1(a,b,c,d,e):

    print(a,b,c,d,e)

def fun2(normal, *args, **kwargs): # by *args we can as many args we want
    print(normal)   # what **kwargs does is, it sends argument in the form of key and value pair.
    for i in args:
        print(i)
    print("\nNow this this that that")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

var1 = ["Saurabh", "Rohan", "Skillf", "hammad"]

norm = "I am a normal Argument and the students are: "
kw = {"kk": "uu", "aa": "bb", "tt":"qq", "lazy": "Me"}

fun2(norm, *var1, **kw)