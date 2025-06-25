# Alireza Nejati
# Saturday , June 21 , 2025

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def main():
    while True:
        date = input('Date: ')
        date = date.strip()
        date = date.rstrip()
        date_parts = date.split(' ')
        if (len(date_parts) == 3):
            if (date_parts[1][len(date_parts[1])-1]) != ',':
                continue
            date_parts[1] = date_parts[1][0:len(date_parts[1])-1]
            if (date_parts[0].capitalize() not in months):
                continue
            else:
                return_number = date_string_generator(date_parts[2], date_parts[0], date_parts[1])
                if (return_number == 0):
                    break
                else:
                    continue
        else:
            try:
                date_parts = date.split('/')
                date_parts[0] = int(date_parts[0])
                return_number = date_string_generator(date_parts[2], date_parts[0], date_parts[1])
                if (return_number == 0):
                    break
                else:
                    continue
            except ValueError:
                continue


def date_string_generator(year, month, day):

    if (month in months):
        for index in range(len(months)):
            if months[index] == month:
                month = index+1
                break

    day = int(day)
    if day > 31:
        return -1
    month = int(month)
    if month > 12:
        return -1
    year = int(year)

    print(f'{year}-{month:02}-{day:02}')
    return 0


main()
