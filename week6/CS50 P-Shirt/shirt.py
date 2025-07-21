# Alireza Nejati (alirezanejatiz27@gmail.com)
# Monday , July 21 , 2025

from sys import argv, exit
from PIL import Image, ImageOps


if len(argv) > 3:
    print('Too many command-line arguments')
    exit(1)
elif len(argv) < 3:
    print('Too few command-line arguments')
    exit(1)
input_image_file_name = argv[1]
output_image_file_name = argv[2]
output_image_file_parts = output_image_file_name.split('.')
input_image_file_parts = input_image_file_name.split('.')
if (output_image_file_parts[-1] == 'bmp'):
    print('Invalid output')
    exit(1)
elif (output_image_file_parts[-1] != input_image_file_parts[-1]):
    print('Input and output have different extensions')
    exit(1)

try:
    shirt_image = Image.open('shirt.png')
    before_image = Image.open(input_image_file_name)
    shirt_size = shirt_image.size
    before_image = ImageOps.fit(before_image, shirt_size)
    before_image.paste(shirt_image, shirt_image)
    before_image.save(output_image_file_name)


except FileNotFoundError:
    print('Input does not exist')
    exit(1)
