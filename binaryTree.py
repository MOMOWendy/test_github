import sys


class TreeNode:
    parent = None
    left = None
    right = None

    def __init__(self, key):
        self.key = key

    def __del__(self):
        print('节点释放了')



class Tree:
    root = None
    size = 0

    def __init__(self):
        self.root = None

    def search(self, key):

        # return the node if the key exists in the tree or None otherwise
        x = self.root
        while x is not None:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return x


    def insert(self, key):

        x = self.root
        y = None
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z = TreeNode(key)
        z.parent = y
        if y is None:
            self.root = z
        elif key < y.key:
            y.left = z
        else:
            y.right = z
        self.size += 1

    def delete(self, key):

        # return the deleted key as the return value
        z = self.search(key)
        if z.left is None:
            self.transplant(z,z.right)
        elif z.right is None:
            self.transplant(z,z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y,y.right)
                y.right = z.right
                z.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            z.left.parent = y


    def transplant(self,u,v):
        if u.parent is None:
            self.root=v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right=v
        if v is not None:
            v.parent=u.parent

    def minimum(self,node):
        while node.left is not None:
            node=node.left
        return node

    # an example for pre-order traverse on tree
    def preOrderTraverse(self, curr_root, operator):
        if (curr_root == None):
            return

        operator(curr_root)
        self.preOrderTraverse(curr_root.left, operator)
        self.preOrderTraverse(curr_root.right, operator)

    def inOrderTraverse(self, curr_root, operator):
        if (curr_root == None):
            return

        self.inOrderTraverse(curr_root.left, operator)
        operator(curr_root)
        self.inOrderTraverse(curr_root.right, operator)

    def postOrderTraverse(self, curr_root, operator):
        if (curr_root == None):
            return

        self.postOrderTraverse(curr_root.left, operator)
        self.postOrderTraverse(curr_root.right, operator)
        operator(curr_root)

    def levelOrderTraverse(self, curr_root, operator):
        if (curr_root == None):
            return

        q = [self.root]
        while len(q) != 0:
            curr_node = q.pop(0)
            operator(curr_node)
            if curr_node.left is not None:
                q.append(curr_node.left)
            if curr_node.right is not None:
                q.append(curr_node.right)
