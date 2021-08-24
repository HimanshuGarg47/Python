# import os
# entries = os.scandir('C:/Users/Himanshu Garg/Documents/Python/')
# print(entries)
# for entry in entries:
#     print(entry.name)
    
    
# from pathlib import Path

# entries = Path('C:/Users/Himanshu Garg/Documents/Python/')
# print(entries)
# for entry in entries.iterdir():
#     print(entry)

# import os

# # List all files in a directory using os.listdir
# basepath = 'C:/Users/Himanshu Garg/Documents/Python/'
# for entry in os.listdir(basepath):
#     #if os.path.isfile(os.path.join(basepath, entry)):
#   print(entry)




# from pathlib import Path

# basepath = Path('C:/Users/Himanshu Garg/Documents/Python/')
# print(basepath)
# files_in_basepath = basepath.iterdir()
# for item in files_in_basepath:
#     if item.is_file():
#         print(item.name)





# import os

# # List all subdirectories using os.listdir
# basepath = 'C:/Users/Himanshu Garg/Documents/Python/'
# for entry in os.listdir(basepath):
#     if os.path.isdir(os.path.join(basepath, entry)):
#         print(entry)





import os
with os.scandir('C:/Users/Himanshu Garg/Documents/Python/') as dir_contents:
    for entry in dir_contents:
       info = entry.stat()
       print(info.st_mtime)