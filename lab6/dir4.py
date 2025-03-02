def lines(text_path):
    with open(text_path, 'r') as file:
        lines_count = file.readlines() 
        print(len(lines_count)) 
#lines(r"C:\Users\Акниет\Labs\lab6\text.txt")  

# Или относительный, если ты запускаешь код из Labs
lines("lab6/text.txt")