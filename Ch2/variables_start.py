# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
#print(f)

# re-declaring the variable works
#f='abc'
#print(f)


# ERROR: variables of different types cannot be combined
#print("hello"+str(123))


# Global vs. local variables in functions
f=0
def somefunction():
    global f
    f='def'
    print(f)
somefunction()
print(f)

#del function deletes assigment(values) of a particular varilble
del f
print(f)
