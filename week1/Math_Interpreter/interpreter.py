# Alireza Nejati (alirezanejatiz27@gamil.com)

Expression = input('Expression: ')

Expression_parts = Expression.split()

X = int(Expression_parts[0])
Y = Expression_parts[1]
Z = int(Expression_parts[2])

result = 0.00

if (Y == '+'):
    result = float(X+Z)
elif (Y == '*'):
    result = float(X*Z)
elif (Y == '/'):
    result = float(X/Z)
elif (Y == '-'):
    result = float(X-Z)

result = round(result, 1)

print(result)
