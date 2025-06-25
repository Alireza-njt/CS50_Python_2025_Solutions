# Alireza Nejati (alirezanejatiz27@gmail.com)
# Wednesday , June 25 , 2025

from sys import argv, exit

answer = 0

if (len(argv)) == 1:
    exit('Too few command-line arguments')
elif (len(argv) > 2):
    exit('Too many command-line arguments')
else:
    file_name = argv[1]
    file_name_components = file_name.split('.')
    if (len(file_name_components) == 1):
        exit('Not a Python file')
    file_type = file_name_components[len(file_name_components)-1]
    if (file_type != 'py'):
        exit('Not a Python file')
    try:
        with open(file_name) as file:
            for line in file:
                line = line.rstrip()
                line = line.strip()
                if line == '' or line.startswith("#"):
                    pass
                else:
                    answer += 1

        print(answer)

    except FileNotFoundError:
        exit('File does not exist')
