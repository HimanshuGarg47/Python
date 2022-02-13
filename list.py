ls = [1,2,3,4,5,55,6]
bs = [9,8,10]
ls.append(7) # append  an single item to list
print(ls)

ls.extend(bs)  # extend list by accepting iterable or list
print(ls)

ls.insert(len(ls),11) # insert number at given position (i,x)
print(ls) 

ls.remove(8)  # remove first occurence of 8 
print(ls)


"""    list.pop([i])
Remove the item at the given position in the list, and return it.

If no index is specified, a.pop() removes and returns the last item in the list.
(The square brackets around the i in the method signature denote that the parameter is optional,
 not that you should type square brackets at that position.   """
 
print(ls.pop(0))   # remove i th position element from list and pop() parameter is optional
print(ls)


# count number of occurence of number x count(x)
print(ls.count(8))




# list.sort(*, key=None, reverse=False)
"""Sort the items of the list in place
(the arguments can be used for sort customization,
 see sorted() for their explanation)."""
ls.sort(reverse=True)
print(f'Sorted list in dec. order  is {ls} ')



# reverse list elements
ls.reverse()
print(ls)


print(ls[-1])
#clear entire array or delete
ls.clear()
print(ls)




# list as Stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

stack.pop()


stack.pop()

stack.pop()

