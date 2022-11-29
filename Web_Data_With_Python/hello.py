
l1 = [1,2,3,4]
l2 = l1
print("Before changing list : Id's of l1 and l2 are: " , id(l1), " " , id(l2))
l2.append(5)
print("l1: ", l1)
print("l2: ", l2)
print("After changing list : Id's of l1 and l2 are: " , id(l1), " " , id(l2))


print("\n\n\n")
t1=(1,2,3,4)
t2=t1
print("Before changing tuple : Id's of t1 and t2 are: " , id(t1), " " , id(t2))
t2 += (5,)
print("t1: ", t1)
print("t2: ", t2)
print("After changing tuple : Id's of t1 and t2 are: " , id(t1), " " , id(t2))


