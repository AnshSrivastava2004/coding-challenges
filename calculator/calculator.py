import sys

def precedence(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    return -1

def operate(val1, val2, op):
    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == '*':
        return val1 * val2
    elif op == '/':
        return val1 / val2
    elif op == '^':
        return val1 ** val2

def evaluateExpr(infix):
    values = []
    ops = []
    i = 0
    while i < len(infix):
        if infix[i] == ' ':
            i += 1
            continue
        elif infix[i] == '(':
            ops.append(infix[i])
        elif infix[i].isdigit():
            val = 0
            while i < len(infix) and infix[i].isdigit():
                val = val * 10 + int(infix[i])
                i += 1
            values.append(val)
            i -= 1
        elif infix[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(operate(val1, val2, op))
            ops.pop()
        else:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(infix[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(operate(val1, val2, op))
            ops.append(infix[i])
        i += 1
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(operate(val1, val2, op))

    return values[-1]

if __name__ == "__main__":
    x = ' '.join(sys.argv[1:])
    print(x)
    print(evaluateExpr(x))