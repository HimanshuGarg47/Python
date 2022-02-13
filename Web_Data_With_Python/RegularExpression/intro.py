import re
import string

hand = open(r"D:\myCode\Python\Web_Data_With_Python\RegularExpression\file1.txt","r+")
for line in hand:
    line = line.rstrip()
    if line.find('From'):
        print(line)
        
        
hand.close()



^ mean starting character
hand = open(r"D:\myCode\Python\Web_Data_With_Python\RegularExpression\file1.txt","r+")
for line in hand:
    line = line.rstrip()
    if re.search('^From',line):
        print(line)
        
        
hand.close()
        
        

# extracting numbers from string
x = "My favourite is 22 and 19 03 0"
lis = re.findall("[0-9]+",x)
for i in lis:
    print(i)
print()
print(lis) 



string = "From: The compleet Bootcamp: 2022"
# To avoid Greedy use ?
lis = re.findall('^F.+?:',string)  #findall('^F.+:',string) This is greedy method as return largest possibel string 
print(lis)



str1 = "From himanshu08@gmail.com 20 302 "
reg = re.findall('\S+@\S+',str1)
print(reg)



# extract hostname with slicing and find method
addr = "From google@com 08-08-2002"
atpos = addr.find('@')
print(atpos)
stpos = addr.find(' ',atpos)
print(stpos)
host = addr[atpos+1:stpos]
print(host)

# second method of doing it by spliting words
words = addr.split()
ur = words[1]
hostname = ur.split('@')
print(hostname[1])
