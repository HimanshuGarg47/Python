import pickle 

cars = ["Maruti", "BMW", "Lamborgini", "Himati"]

file = 'pickling.pkl'
fileobj = open(file, 'wb')
# print(dir(fileobj))
pickle.dump(cars, fileobj)
fileobj.close()

