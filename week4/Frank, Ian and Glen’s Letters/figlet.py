# Alireza Nejati
# Wednesday , June 18 , 2025

from pyfiglet import Figlet
import sys
import random

F = Figlet()

Fonts = F.getFonts()

if (len(sys.argv) == 1 or len(sys.argv) == 3):
    if (len(sys.argv) == 1):
        text = input()
        random_font = random.choice(Fonts)
        F.setFont(font=random_font)
        print(F.renderText(text))
    else:
        if (sys.argv[1] != '-f'):
            print('Invalid usage')
            sys.exit(2025)
        if (sys.argv[2] in Fonts):
            text = input()
            F.setFont(font=sys.argv[2])
            print(F.renderText(text))
        else:
            print('Invalid usage')
            sys.exit(2025)

else:
    print('Invalid usage')
    sys.exit(2025)
