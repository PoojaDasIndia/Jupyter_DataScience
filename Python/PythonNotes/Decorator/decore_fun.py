"""
A decorator is a function that accpet a function as parameter and reture function.
we used @function_nam,e to specify a decoratoe to be applied to other function.

"""
#decore function parameter is a function
from unittest import result


def decor(num):
    #inner function
    def inner():
        print("Before")
        num() #num function call
        print("After")

    # decore function return inner function
    return inner


# normal function  we need to enhance in it without chaning it .
# create decortor  above it decore is  normal function which take parameter  as num function 
# and inside it a inner fun and tuen a function

@decor  # bas bata h ye decore ko bhi call karna h 
def num():
    print("1 Pooja")
    print("2 Das")


# print("*****calling 1 way decore function******")

# result=decor(num)
# result()

# print("******calling 2 way*************")
# num=decor(num)
# num()

print("****calling 3 way  best way********")
num()