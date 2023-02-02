# Python Program to create 100 folders for 100 days and a README.md file in each folder
import os
import sys


for day in range(1, 101):
    path = f"Day {day}"
    if not os.path.exists(path):
        os.mkdir(path)
        with open(f"{path}/README.md", 'w') as fp:
            # uncomment if you want empty file
            fp.write(f'# {path} of 100.')
    else:
        print(f'Directory "{path}" existed. Skipped')


# name = sys.argv[1] # folder name

# if not os.path.exists(name): # Check if folder exists
#     os.mkdir(name) # if not then create one

# os.chdir(name) # change directory to the folder

# # option to create test_[name].py for testing purpose
# if (len(sys.argv) == 3 and sys.argv[2] == '-t'):
#     os.system(f"code test_{name}.py")

# # Open the file
# os.system(f"code {name}.py")

# # remain the currect directory after exit program
# os.system("/bin/bash")