import operator

calculator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }

def prefix_cal(expression) :

    op, n1, n2 = expression.split()

    result = calculator[op](float(n1), float(n2))

    return result

print(prefix_cal('+ 10 7'))
