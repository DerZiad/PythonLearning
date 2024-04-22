import random

condition = True

if condition:
    print("True")
else:
    print("False")


x = 5
condition = x == 5 # = Assertion, == Equality

if condition:
    print("True")
else:
    print("False")



if x == 5:
    print("True")
else:
    print("False")

#################################################################################

x = random.randint(1,3)

#if x == 1:
#    print(" X = 1")
#else:
#    if x == 2:
#        print(" X = 3")
#    else:
#        print(" X = 3")

if x == 1:
    print("X == 1")
    print()
    print()
elif x == 2:
    print("X == 2")
    print()
    print()
else:
    print("X == 3")
    print()
    print()


####################### Another way

x = random.randint(1,4)

if x % 2 == 0:
    y = 1
else:
    y = -1

y = 1 if(x % 2 == 0) else -1





