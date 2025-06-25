# Alireza Nejati (alirezanejatiz27@gamil.com)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    result = d[1:len(d)]
    return float(result)  # input : $50.00 --------->>> output : 50.00 (float version)


def percent_to_float(p):
    result = p[0:len(p)-1]
    result = float(result)  # input : 15% --------->>> output : 0.15 (float version)
    return result/100


main()
