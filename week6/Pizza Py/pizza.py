# Alireza Nejati (alirezanejatiz27@gmail.com)
# Wednesday , June 25 , 2025

from sys import argv, exit
from tabulate import tabulate

if (len(argv)) == 1:
    exit('Too few command-line arguments')
elif (len(argv) > 2):
    exit('Too many command-line arguments')
else:
    file_name = argv[1]
    file_name_components = file_name.split('.')
    if (len(file_name_components) == 1):
        exit('Not a CSV file')
    file_type = file_name_components[len(file_name_components)-1]
    if (file_type != 'csv'):
        exit('Not a CSV file')
    try:
        i = 0
        headers = []
        contents = []
        with open(file_name) as file:
            for line in file:
                line = line.strip()
                if i == 0:
                    headers = line.split(',')
                else:
                    line_list = line.split(',')
                    contents.append(line_list)
                i += 1
        print(tabulate(contents, headers, tablefmt="grid"))
    except FileNotFoundError:
        exit('File does not exist')
