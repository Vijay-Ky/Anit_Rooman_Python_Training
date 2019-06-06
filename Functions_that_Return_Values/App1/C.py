"""
The return Statement

1. The statement return [expression] exits a
   function, optionally passing back an
   expression to the caller
-------------------------------------
-You can return a value from a function as follows
"""
def sum(arg1, arg2):
    "Add both the parameters and return them"
    total = arg1 + arg2
    print("inside the function",  total)
    return total
#now we can call sum function
total = sum(10, 20)
print("Outside the function", total)



