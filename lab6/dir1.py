import os
def directs(path):
    print([dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path,dir))])
    print([fil for fil in os.listdir(path) if os.path.isfile(os.path.join(path,fil))])
    print(os.listdir(path))
directs("Labs/lab6")