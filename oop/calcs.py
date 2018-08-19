PRIORITY = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1, "^": 0, "±": -1}


class Calculator:
    def __init__(self, opcodes, operators=None):
        self.opcodes = opcodes
        self.operators = operators if operators is not None else []
        self.postfix_form = self._infix_to_postfix(opcodes)
        self.graph = self._build_graph()

    def __str__(self) -> str:
        return ''.join(self.postfix_form).replace('±', '-')

    def optimise(self):
        for operator in self.operators:
            self.opcodes = operator.process(self.opcodes)

    def validate(self) -> bool:
        if self._brackets_balance(self.opcodes) and self._forbidden_operations(self.postfix_form) and self.graph:
            return True
        else:
            return False

    def _brackets_balance(self, expression):
        stack = []

        for tok in expression:
            if tok == '(':
                stack.append(tok)
            if tok == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    return False

        if len(stack) != 0:
            return False

        return True

    def _forbidden_operations(self, postfix_form):
        if '0/' in ''.join(postfix_form):
            return False
        return True

    def _infix_to_postfix(self, tokens):

        stack = []
        postfix_list = []
        unary_flag = False

        try:
            for tkn in tokens:
                if tkn.isalnum():
                    postfix_list.append(tkn)
                    unary_flag = False
                elif tkn == '(':
                    stack.append(tkn)
                    unary_flag = True
                elif tkn == ')':
                    top_tkn = stack.pop()
                    while top_tkn != '(':
                        postfix_list.append(top_tkn)
                        top_tkn = stack.pop()
                elif tkn in PRIORITY.keys():
                    # case of unary minus
                    if tkn == '-' and (len(postfix_list) == 0 or unary_flag):
                        stack.append('±')
                    else:
                        while len(stack) != 0 and PRIORITY[stack[-1]] >= PRIORITY[tkn]:
                            postfix_list.append(stack.pop())
                        stack.append(tkn)
        except IndexError:
            return 'Check the correctness of the input expression.'

        while len(stack) != 0:
            postfix_list.append(stack.pop())

        return postfix_list

    def _build_graph(self):
        reversed_postfix = self.postfix_form[::-1]

        graph = Tree(Node(reversed_postfix[0]))

        def fillin_subtree(root, tok_index=1):
            tok = reversed_postfix[tok_index]

            if not root.right:
                root.right = Node(tok)
                if tok in PRIORITY:
                    tok_index = fillin_subtree(root.right, tok_index + 1)

            if not root.left:
                tok_index += 1
                tok = reversed_postfix[tok_index]
                root.left = Node(tok)
                if tok in PRIORITY:
                    fillin_subtree(root.left, tok_index + 1)

            # print(root.value, root.right.value, root.left.value)

            return tok_index

        try:
            fillin_subtree(graph.root)
        except IndexError:
            return False

        return graph


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self._traverse(self.root)

    def _traverse(self, root, acc=''):
        if root.left:
            if root.left.value in PRIORITY:
                acc = self._traverse(root.left, acc)
            else:
                acc += root.left.value

        acc += root.value

        if root.right:
            if root.right.value in PRIORITY:
                acc = self._traverse(root.right, acc)
            else:
                acc += root.right.value
        return acc


class Node:
    def __init__(self, val, left=None,right=None):
        self.value = val
        self.left = left
        self.right = right


def test():
    str_check_list = [
        ("a", "a"),
        ("-a", "a-"),
        ("(a*(b/c)+((d-f)/k))", "abc/*df-k/+"),
        ("(a)", "a"),
        ("a*(b+c)", "abc+*"),
        ("(a*(b/c)+((d-f)/k))*(h*(g-r))", "abc/*df-k/+hgr-**"),
        ("(x*y)/(j*z)+g", "xy*jz*/g+"),
        ("a-(b+c)", "abc+-"),
        ("a/(b+c)", "abc+/"),
        ("a^(b+c)", "abc+^")
    ]
    for (case, exp) in str_check_list:
        tokens = list(case)
        calc = Calculator(tokens)

        if str(calc) != exp:
            print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')


def test1():
    validate_check_list = [
        ('a+2', True),
        ('a-(-2)', True),
        ('a+2-', False),
        ('a+(2+(3+5)', False),
        ('a^2', True),
        ('a^(-2)', True),
        ('-a-2', True),
        ('6/0', False),
        ('a/(b-b)', True)
    ]

    for case, exp in validate_check_list:
        tokens = list(case)

        calc = Calculator(tokens).validate()

        if calc != exp:
            print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')


def test2():
    expr = "-(-1)"
    calc = Calculator(expr)
    print(calc.graph)


if __name__ == '__main__':
    test1()
