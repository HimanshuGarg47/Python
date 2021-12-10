class student:
    def __init__(self,name) :
        self.__name = name
    
    def display_name(self):
        print(self.__name)
        

s1 = student("Himanshu")
s1.display_name()
print(s1._student__name)
print(dir(s1))        
    
