"""Using split() Method
    --------------------

    
The split() method is useful for getting multiple inputs from users. The syntax is given below.

Syntax -


input().split(separator, maxsplit)  
Parameters -

The separator parameter breaks the input by the specified separator. By default, whitespace is the specified separator.
The split() method is used to split the Python string, but we can use it to get the multiple values.
    """









# taking two inputs at a time  
a, b, c = input("Enter three values: ").split()  
print("Enter Your First Name: ", a)  
print("Enter Your Last Name: ", b)  
print("Enter Your Class: ", c)  
print()  
   
# taking three inputs at a time  
x, y, z = input("Enter three values: ").split()  
print("Total number of students: ", x)  
print("Number of passed student : ", y)  
print("Number of failed student : ", z)  
print()  
   
# taking four inputs at a time  
a, b, c, d = input("Enter four values: ").split()  
print("First number is {}, second number is {} third is {} and fourth is {}".format(a, b, c, d))  
print()  