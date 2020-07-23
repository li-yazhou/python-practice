# postfix expression compute
def postfix(s):
    stack = []

    for i in s:
        # if type(i) is int:
        if i.isdigit():
            stack.append(int(i))
        else:
            # assume all operators are binary
            num_1 = stack.pop()
            num_2 = stack.pop()
            result = compute(num_1, num_2, i)
            stack.append(int(result))
    return stack[0]

def compute(first, second, operator):
    if operator == '+':
        result = first + second
    elif operator == '-':
        result = second - first
    elif operator == '*':
        result = second * first
    elif operator == '/':
        result = second / first
    else :
        raise ValueError('operator is wrong!')
    return result

if __name__ == '__main__':
    string = '435*+'
    result = postfix(string)
    print(result)
    
