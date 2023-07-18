# ex_5_0.py

def line_count(infile):
    with open(infile, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        print("Number of lines in the file:", line_count)



