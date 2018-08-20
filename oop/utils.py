PRIORITY = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1, "^": 0, "±": -1}


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


def build_graph(postfix_form):
    reversed_postfix = postfix_form[::-1]

    graph = Tree(Node(reversed_postfix[0]))

    def fillin_subtree(root, tok_index=1):
        tok = reversed_postfix[tok_index]

        if not root.right:
            root.right = Node(tok)
            if tok in PRIORITY:
                tok_index = fillin_subtree(root.right, tok_index + 1)

        if root.value != '±' and not root.left:
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
