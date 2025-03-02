import os
def exist(path):
    if os.path.exists(path):
        print("Exists")
        print("File:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path doesnt exist")
exist("Labs/lab6")