# Building Hello World
def main():
    print ("Hello World!")

if __name__ == '__main__':
    main()
    print ("Hi")

print("Out of main function")

# Variables and Expressions
f=0
print (f)

f= "abc"
print (f)

print ("some string" + str(123))

def somefunction():
    global f
    f = "fstring"
    print (f)

somefunction()
print (f)

del (f)
print (f)

#Python Functions
def func1(arg1, arg2):
    print (arg1," ",arg2)
    return arg1+arg2

func1(10,20)
print (func1(5,6))
print (func1)

def func2(x):
    cube = x*x*x
    return cube

print (func2(3))

def power(y, x):
    result = 1
    for i in range (0,x,1):
        result = result * y

    return result

power(3,2)

def multi_list(*args):
    result=0
    for x in args:
        result=result+x
    return result

print (multi_list(4,5,6,7))
