PRIORITY = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}


def brackets_trim(input_data: str) -> str:
    return postfix_to_infix(infix_to_postfix(input_data))


def infix_to_postfix(expr):

    stack = []
    postfix_list = []
    tokens = expr.split() if ' ' in expr else expr

    try:
        for tkn in tokens:
            if tkn.isalpha():
                postfix_list.append(tkn)
            elif tkn == '(':
                stack.append(tkn)
            elif tkn == ')':
                top_tkn = stack.pop()
                while top_tkn != '(':
                    postfix_list.append(top_tkn)
                    top_tkn = stack.pop()
            elif tkn in PRIORITY.keys():
                while len(stack) != 0 and PRIORITY[stack[-1]] >= PRIORITY[tkn]:
                    postfix_list.append(stack.pop())
                stack.append(tkn)
    except IndexError:
        return 'Check the correctness of the input expression.'

    while len(stack) != 0:
        postfix_list.append(stack.pop())

    return ' '.join(postfix_list)


def postfix_to_infix(postfix_list):
    stack = []

    try:
        for tkn in postfix_list:
            if tkn.isalpha():
                stack.append(tkn)
            elif tkn in PRIORITY.keys():
                operand2 = stack.pop()
                operand1 = stack.pop()

                # check PRIORITY
                if is_operand_priority_lower(operand1, tkn):
                    operand1 = '( {} )'.format(operand1)
                if is_operand_priority_lower(operand2, tkn):
                    operand2 = '( {} )'.format(operand2)

                stack.append('{} {} {}'.format(operand1, tkn, operand2))

        return stack.pop()

    except IndexError:
        return 'Check the correctness of the input expression.'


def is_operand_priority_lower(operand, operator):
    for i, tkn in enumerate(operand):
        if tkn in PRIORITY.keys() and tkn != '(' and PRIORITY[tkn] < PRIORITY[operator]:
            return True
    return False


if __name__ == '__main__':
    print(brackets_trim("(a*(b/c)+((d-f)/k))"))




