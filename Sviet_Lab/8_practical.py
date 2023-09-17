''' Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [ Formula: 
c/5 = f-32/9]
'''

cel = int(input("Enter celcius\n"))
fahr = (cel*(9//5))+32
print('fahrenheit value is {}'.format(fahr))

