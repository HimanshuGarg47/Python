
"""
    Syntax:

    print(object(s), sep=' ', end='\n', file=file, flush=False)

    For your better understanding of the syntax here we have defined few keywords of the above statement:

    object(s)-  are the values to be printed on the screen. They are converted to strings before getting printed.

    sep keyword-  is used to specify how to separate the objects inside the same print statement. By default, we have it as sep=' ', a space between two objects.

    end - is used to print a particular thing after all the values are printed. By default, we have end as \n, which provides a new line after each print() statement.

    file - is used to specify where to display the output. By default, it is sys.stdout (which is the screen).

    flush - specifies the boolean expression if the output is False or True. By default, it is False. In Python, the output from the print() goes into a buffer. Using the flush= True parameter helps in flushing the buffer as soon as we use the print() statement.
    """

print(1, 2, 3)  # here spaces are by default

print("Hello","Hello","Tab",sep = " ", end="\n")
print("Hello", end="\n")



students = 5000
print("Scaler has " + str(students) + " employees")




# Here we take two variables and do certain operations with it.                                                                                                                        
x = 3
y = 12
mul = x * y
print('The value of x is {} and y is {}'.format(x, y))
# Here we are specifying the order of the variables.
print('{2} is the multiplication of {0} and {1}'.format(x, y, mul))
# We can even use keyword arguments to format strings.
print('Hey! Welcome to {company}. In this article we will learn about {language}'.format(company='Scaler', language='Python'))







