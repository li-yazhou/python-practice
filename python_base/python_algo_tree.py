
class Node(object):
    '''
        树的表示法：孩子表示法
        另外两种表示法：双亲表示法、孩子兄弟表示法
    '''
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children

    def add_children(self, children):
        self.children = children

    def depth_first_search(self, node):
        if node: print(node.value)
        if node.children:
            for i in range(len(node.children)):
                self.depth_first_search(node.children[i])

    def width_first_search(self, node):
        if node: print(node.value)
        if node.children:
            for i in range(len(node.children)):
                print(node.children[i].value)


def test_node():
    root = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    a_children = [b,c]
    b_children = [d]
    c_children = [e,f]

    root.add_children(a_children)
    b.add_children(b_children)
    c.add_children(c_children)

    print(root.value)
    print(root.children[0].value)

    Node().depth_first_search(root)




class BiTree(object):

    def __init__(self, value=None, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def add_left_child(self, left_child):
        self.left_child = left_child

    def add_right_child(self, right_child):
        self.right_child = right_child

    def add_children(self, left_child, right_child):
        self.add_left_child(left_child)
        self.add_right_child(right_child)


    def pre_order_traverse(self, node):
        if node is None: return
        print(node.value)
        self.pre_order_traverse(node.left_child)
        self.pre_order_traverse(node.right_child)


    def in_order_traverse(self, node):
        if node is None: return
        self.in_order_traverse(node.left_child)
        print(node.value)
        self.in_order_traverse(node.right_child)

    def post_order_traverse(self, node):
        if node is None: return
        self.post_order_traverse(node.left_child)
        self.post_order_traverse(node.right_child)
        print(node.value)


def test_bitree():
    a = BiTree('A')
    b = BiTree('B')
    c = BiTree('C')
    d = BiTree('D')
    e = BiTree('E')
    f = BiTree('F')

    b.add_left_child(d)
    c.add_children(e,f)
    a.add_children(b,c)

    a.pre_order_traverse(a)
    print('-'*10)
    a.in_order_traverse(a)
    print('-'*10)
    a.post_order_traverse(a)


def main():
    # test_node()
    test_bitree()





if __name__ == '__main__':
    main()








