# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import os

path = "C:\\Users\\Abdul Mateen\\Downloads\\python-101-main"

for path, subdirs, files in os.walk(path):
    for name in files:
        print(os.path.join(path, name))