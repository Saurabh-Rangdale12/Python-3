# map(function, iterable)

# nums = ["3", "78", "33"]
# nums = list(map(int, nums))  # This is map which converts all elements of nums to int
#
# nums[2] = nums[2] + 1
# print(nums[2])
#
# def sq(a):
#     return a*a
#
# num = [2,3,5,7,21,22,55]
#
# square = list(map(sq, num))
# print(square)
#
# num2 = [2,3,5,7,21,22,55]
# squ = list(map(lambda x: x*x, num2))
# print(squ)
#
# def cube(a):
#     return a*a*a
#
# func = [sq, cube]
# num3 = [2,3,5,7,21,22,55]
#
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)
#

#  -----------FLITER------------------

# ilter():-
# "A filter function in Python tests a specific user-defined condition for a function and returns an iterable for the
# elements and values that satisfy the condition or, in other words, return true."
# filter(function, iterable)

# list_1 = [1,3,4,5,6,7,9,12]
# def is_greate_5(num):
#     return num>5  # it return true or false
#
# gr_than_5 = list(filter(is_greate_5, list_1))
# print(gr_than_5)

# ----------------Reduce---------------------
# "Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".
# reduce(function, iterable)

from functools import reduce

list1 = [1,2,3,4,2,5,6]
num = reduce(lambda x, y: x+y, list1)

# num = reduce(lambda x,y,z: x+y+z, list1) why this is not working :(

# num = 0
# for i in list1:
#     print(i, end=" ")
#     num = num + i

print(num)

# sum3 = lambda x,y,z: x+y+z
# print(sum3(4,5,6))
