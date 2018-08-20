from oop.utils import PRIORITY
from oop.utils import build_graph
from oop.optimisers import DoubleNegativeOptimiser, IntegerCostantsOptimiser, SimplifierOptimiser


class Calculator:
    def __init__(self, opcodes, operators=None):
        self.opcodes = opcodes
        self.operators = operators if operators is not None else []
        self.postfix_form = self._infix_to_postfix(opcodes)
        self.graph = build_graph(self.postfix_form)

    def __str__(self) -> str:
        return ''.join(self.postfix_form).replace('±', '-')

    def optimise(self):
        for operator in self.operators:
            self.postfix_form = operator.process(self.postfix_form)

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
                    if len(stack) and stack[-1] == '±':
                        postfix_list.append(stack.pop())
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
    double_negate_tests = [
        ('-(-a)', 'a'),
        ('-(-5)', '5'),
        ('-(a+b)+c-(-d)', 'ab+-c+d+'),
    ]

    for case, exp in double_negate_tests:
        tokens = list(case)
        calc = Calculator(tokens, [DoubleNegativeOptimiser()])
        calc.optimise()

        if str(calc) != exp:
            print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')


def test3():
    integer_constant_optimiser_tests = [
        (['1'], ['1']),
        (['1', '+', '2'], ['3']),
        (['1', '-', '2'], ['1-']),
        (['2', '*', '2'], ['4']),
        (['2', '/', '2'], ['1.0']),
        (['2', '^', '10'], ['1024']),
        (['a', '+', '2', '*', '4'], ['a8+', '8a+']),
    ]

    for case, exp in integer_constant_optimiser_tests:
        calc = Calculator(case, [DoubleNegativeOptimiser(), IntegerCostantsOptimiser()])

        calc.optimise()

        if str(calc) not in exp:
            print(f'Error in case for "{case}". Actual "{calc}", expected one of {exp}')


def test4():
    simplifier_optimiser_test = [
        ('a+0', ['a']),
        ('a*1', ['a']),
        ('a*0', ['0']),
        ('b/b', ['1']),
        ('a-a', ['0']),
        ('a+(b-b)', ['a']),
        ('a+(7-6-1)', ['a']),
        ('a^0', ['1']),
        ('a-(-(-a))', ['0']),
    ]

    for case, exps in simplifier_optimiser_test:
        tokens = list(case)
        calc = Calculator(tokens, [DoubleNegativeOptimiser(), IntegerCostantsOptimiser(), SimplifierOptimiser()])

        calc.optimise()

        if str(calc) not in exps:
            print(f'Error in case for "{case}". Actual "{calc}", expected one of {exps}')


if __name__ == '__main__':
    test()
