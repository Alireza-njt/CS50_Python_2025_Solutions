# Alireza Nejati (alirezanejatiz27@gamil.com)

file_name = input('File name: ')
file_name_parts = file_name.split('.')
if (len(file_name_parts) >= 2):
    file_type = file_name_parts[len(file_name_parts)-1]
else:
    file_type = ''

file_type = file_type.lower()  # To convert all uppercase letters in a string to lowercase
file_type = file_type.strip()  # To remove spaces at the beginning and end of a string


if (file_type == 'gif'):
    print('image/gif')
elif (file_type == 'jpg' or file_type == 'jpeg'):
    print('image/jpeg')
elif (file_type == 'png'):
    print('image/png')
elif (file_type == 'pdf'):
    print('application/pdf')
elif (file_type == 'txt'):
    print('text/plain')
elif (file_type == 'zip'):
    print('application/zip')
elif (file_type == 'bin' or file_type == ''):
    print('application/octet-stream')
