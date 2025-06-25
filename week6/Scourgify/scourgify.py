# Alireza Nejati (alirezanejatiz27@gmail.com)
# Wednesday , June 25 , 2025

"""
“Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage. “Scourgify.”
 A few feathers and droppings vanished.

— Harry Potter and the Order of the Phoenix
"""

from sys import argv, exit
import csv

students = []

if (len(argv)) <= 2:
    exit('Too few command-line arguments')
elif (len(argv) > 3):
    exit('Too many command-line arguments')
else:
    old_file_name = argv[1]
    new_file_name = argv[2]
    old_file_name_components = old_file_name.split('.')
    if (len(old_file_name_components) == 1):
        exit('Not a CSV file')
    old_file_type = old_file_name_components[len(old_file_name_components)-1]
    if (old_file_type != 'csv'):
        exit('Not a CSV file')
    try:
        i = 0
        with open(old_file_name) as old_file:
            for line in old_file:
                if (i > 0):
                    line = line.strip()
                    line = line.split(',')
                    last = line[0]
                    last = last[1:]
                    first = line[1]
                    first = first[1:len(first)-1]
                    house = line[2]
                    students.append({'first': first, 'last': last, 'house': house})
                i -= -1

    except FileNotFoundError:
        massage = f'Could not read {old_file_name}'
        exit(massage)

    with open(new_file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for i in range(len(students)):
            student = students[i]
            writer.writerow({'first': student['first'],
                            'last': student['last'], 'house': student['house']})
