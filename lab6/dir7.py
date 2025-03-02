import shutil
def copy_file(source, destination):
    shutil.copy(source, destination)
copy_file("text.txt", "copy.txt")