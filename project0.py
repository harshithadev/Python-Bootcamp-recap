# Self Project : Populate folder with files named from project7.py to project100.py 

import os  

# print("Creating 100 python project files... ")
# for i in range(7,101):
#     # str = "touch project"+str(i)+".py"
#     os.system(f"touch project{i}.py")
# print("Done !")

# adding the first comment line. 
print("Writing first comment in each project file created...")
for i in range(7,101):
    os.system(f'echo "# Project {i} : " > project{i}.py')
print("Done!")
