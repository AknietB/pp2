import os
def check(path):
    print(os.path.exists(path))
    print(os.access(path, os.R_OK))
    print(os.access(path, os.W_OK))
    print(os.access(path, os.X_OK))
check("Labs/lab6")