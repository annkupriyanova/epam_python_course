from oop.utils import build_graph


class AbstractOptimiser:
    def process(self, postfix_form):
        g = self.pre_process(postfix_form)

        result = self.process_internal(postfix_form, g)

        return self.post_process(result)

    def pre_process(self, postfix_form):
        return build_graph(postfix_form)

    def process_internal(self, graph):
        return graph

    def post_process(self, result):
        return result


class DoubleNegativeOptimiser(AbstractOptimiser):
    def process_internal(self, postfix_form, graph=None):
        postfix = []
        i = 0

        while i < len(postfix_form):
            tok = postfix_form[i]
            # case '±±'
            if tok == '±' and i+1 < len(postfix_form) and postfix_form[i+1] == '±':
                i += 1
            # case '±-'
            elif tok == '±' and i+1 < len(postfix_form) and postfix_form[i+1] == '-':
                postfix.append('+')
                i += 1
            else:
                postfix.append(tok)
            i += 1

        return postfix


class IntegerCostantsOptimiser(AbstractOptimiser):
    def process_internal(self, postfix_form, graph=None):
        stack = []

        for tok in postfix_form:
            if tok.isalnum():
                stack.append(tok)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if operand1.isdigit() and operand2.isdigit():
                    result = self._calculate(tok, int(operand1), int(operand2))
                    if result < 0:
                        stack.append(f'{abs(result)}-')
                    else:
                        stack.append(str(result))
                else:
                    stack.append(f'{operand1}{operand2}{tok}')

        return list(stack.pop())

    def _calculate(self, operator, op1, op2):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return op1 / op2
        elif operator == '^':
            return op1**op2


class SimplifierOptimiser(AbstractOptimiser):
    def process_internal(self, postfix_form, graph):
        graph = self._ones_and_zeros(graph)
        graph = self._double_operand(graph)
        graph = self._ones_and_zeros(graph)

        return graph

    def post_process(self, graph):
        def _make_postfix(root, postfix=[]):
            if not root:
                return postfix
            if root.left:
                postfix = _make_postfix(root.left)
            if root.right:
                postfix = _make_postfix(root.right)

            postfix.append(root.value)

            return postfix

        return _make_postfix(graph.root)

    def _ones_and_zeros(self, graph):
        def _subtree_traverse(root):
            if not root:
                return None

            # left subtree
            if root.left:
                root.left = _subtree_traverse(root.left)
            # right subtree
            if root.right:
                root.right = _subtree_traverse(root.right)

            if root.right and root.right.value in ['0', '1']:
                # cases +0, -0, *0, ^0
                if root.right.value == '0':
                    if root.value in ['+', '-']:
                        root = root.left
                    elif root.value == '*':
                        root.value = '0'
                        root.right = None
                        root.left = None
                    elif root.value == '^':
                        root.value = '1'
                        root.right = None
                        root.left = None
                # cases *1, /1, ^1
                elif root.right.value == '1':
                    if root.value in ['*', '/', '^']:
                        root = root.left

                return root
            return root

        graph.root = _subtree_traverse(graph.root)
        return graph

    def _double_operand(self, graph):
        def _subtrees_equal(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is not None and root2 is not None:
                if root1.value == root2.value:
                    return _subtrees_equal(root1.left, root2.left) and _subtrees_equal(root1.right, root2.right)

            return False

        def _find_doubles(root):
            if not root:
                return None
            if root.left:
                root.left = _find_doubles(root.left)
            if root.right:
                root.right = _find_doubles(root.right)

            if root.value in ['-', '/'] and _subtrees_equal(root.left, root.right):
                if root.value == '-':
                    root.value = '0'
                    root.left = None
                    root.right = None
                elif root.value == '/':
                    root.value = '1'
                    root.left = None
                    root.right = None

            return root

        graph.root = _find_doubles(graph.root)
        return graph
