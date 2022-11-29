
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

print("Hello","Hello","Tab",sep = " ", end="\n")
print("Hello", end="\t")




