import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print(os.getcwd())
with open(f"{dir_path}\graph\pdfs\kd.pdf", 'wb') as f:
    f.write("ka")
    f.close()