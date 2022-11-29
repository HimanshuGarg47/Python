lis = [1,2,3]

# for i in lis:
#     print(i,end="\n")

itera = lis.__iter__()
print(dir(itera))
while True:
    try:
        print(next(itera))
    except StopIteration:
        print("Stoped")
        break