# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

'''
Five hundred twenty-five thousand, six hundred minutes
Five hundred twenty-five thousand moments so dear
Five hundred twenty-five thousand, six hundred minutes
How do you measure, measure a year?

— “Seasons of Love,” Rent
'''

from datetime import date
import sys
import inflect


def main():
    try:
        input_date = input('Date: ')
        input_date = date.fromisoformat(input_date)
    except ValueError:
        sys.exit("Invalid input.")
    total_min = (date.today() - input_date).days * 24 * 60
    engine = inflect.engine()
    result = f"{engine.number_to_words(total_min, andword='').capitalize()} {engine.plural('minute', total_min)}"
    print(result)


if __name__ == "__main__":
    main()
