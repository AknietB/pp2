import os
def delete_file(file_path):
    os.remove(file_path)
delete_file("text.txt")