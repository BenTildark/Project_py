import os, re

current_dir = os.listdir(os.getcwd())
print(current_dir)
if re.search("test.py", str(current_dir)):
	print("True")
else:
	print("False")


