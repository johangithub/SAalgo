class BST:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            while cur:
                print(cur.val)
                if cur.val > node.val:
                    print("{} is greater than {}".format(cur.val, node.val))
                    if cur.left:
                        cur = cur.left
                    else:
                        print("Added {} left of {}".format(node.val, cur.val))
                        cur.left = node
                        cur = None
                elif cur.val < node.val:
                    print("{} is less than {}".format(cur.val, node.val))
                    if cur.right:
                        cur = cur.right
                    else:
                        print("Added {} right of {}".format(node.val, cur.val))
                        cur.right = node
                        cur = None
    def find(self, val):
        cur = self.root
        path = []
        while cur:
            path.append(cur.val)
            if cur.val > val:
                cur = cur.left
            elif cur.val < val:
                cur = cur.right
            elif cur.val == val:
                cur = None
        print('Found {} after {}'.format(val, path))

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return str(self.val)

l = [5, 1,3,7,10,2]
root = None
tree = BST()
for i in l:
    tree.add(Node(i))
print(tree.root)
print(tree.root.left)
print(tree.root.left.right)

tree.add(Node(7.5))

tree.find(7.5)