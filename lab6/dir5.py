def write_list(file_path, list):
    with open(file_path,'w') as file:
        for elements in list:
            file.write(elements+'\n')
write_list("Labs/lab6/text.txt",["Akniet","Barakhan","Pen"])