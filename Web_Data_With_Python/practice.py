import os

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
# print(os.getcwd())
# with open(f"{dir_path}\graph\pdfs\kd.pdf", 'wb') as f:
#     f.write("ka")
#     f.close()

filepath = './dir/subdir/filename.ext'
dirname = os.path.dirname(filepath)
print(dirname)


lnkhref = "onenote/mypdf.pdf"
dir_path = os.path.dirname(os.path.realpath(__file__))
dirname = os.path.dirname(lnkhref)
path = f"{dir_path}\{dirname}\{os.path.basename(lnkhref)}"
print(path)

# checking if the directory demo_folder
# exist or not.
if not os.path.exists("path/to/demo_folder"):
	
	# if the demo_folder directory is not present
	# then create it.
	os.makedirs("path/to/demo_folder")
