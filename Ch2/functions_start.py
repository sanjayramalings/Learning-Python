#
# Example file for working with functions
#

# define a basic function
def fun1():
        print("I am a function")
        #it doesnt return a value

# function that takes arguments
def fun2(arg1,arg2):
    print(arg1," ",arg2)

# function that returns a value
def cube(x):
    return x+x+x


# function with default value for an argument
def power(num,x=1):
    result = 1
    for i in range (x):
            result=result*num
    return result

#function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result = result+x
    return result



fun1()
print ((fun1()))
print (fun1)

fun2(1,2)
print((fun2(1,2)))
print(cube(3))

print(power(2))
print(power(2,3))
print(power(x=5,num=10))


print(multi_add(1,3,4,2,323))