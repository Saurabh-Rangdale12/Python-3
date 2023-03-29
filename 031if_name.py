#  A __name__ is a built-in variable that returns us the name of the module being used.
import file3

print("__name in file3 is set to "+__name__)

t = file3.add(8, 45)
print(t)

# to solve above problem we use __name__
