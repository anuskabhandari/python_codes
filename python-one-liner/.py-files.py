#Get all .py files in a directory
import os
py_files = [f for f in os.listdir('.') if f.endswith('.py')]
print(py_files)