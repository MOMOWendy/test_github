# from binaryTree import Tree
from tree.binaryTree import Tree
import time

def test_Insert():
    tree = Tree()

    input = [12, 5, 2, 9, 18, 15, 13, 17, 19]
    for each in input:
        tree.insert(each)
    assert tree.size == 9

    actual = []
    tree.preOrderTraverse(tree.root, lambda node: actual.append(node.key))

    expected = [12, 5, 2, 9, 18, 15, 13, 17, 19]
    assert actual == expected



def test_Delete():
    tree = Tree()

    input = [12, 5, 18, 2, 9, 15, 19, 13, 17]
    for each in input:
        tree.insert(each)

    tree.delete(17)
    print('17')
    tree.delete(15)
    print('15')
    time.sleep()

    # 这个你写错了吧!!
    expected = [2, 5, 9, 12, 13, 18, 19]
    actual = []
    tree.preOrderTraverse(tree.root, lambda node: actual.append(node.key))
    print(actual)


def test_Search():
    tree = Tree()

    input = [12, 5, 18, 2, 9, 15, 19, 13, 17]
    for each in input:
        tree.insert(each)

    node = tree.search(15)
    assert node.key == 15

    node = tree.search(100)
    assert node == None


def test_PreOrderTraverse():
    tree = Tree()

    input = [12, 5, 2, 9, 18, 15, 13, 17, 19]
    for each in input:
        tree.insert(each)

    actual = []
    tree.preOrderTraverse(tree.root, lambda node: actual.append(node.key))

    expected = [12, 5, 2, 9, 18, 15, 13, 17, 19]
    assert actual == expected


def test_InOrderTraverse():
    tree = Tree()

    input = [12, 5, 2, 9, 18, 15, 13, 17, 19]
    for each in input:
        tree.insert(each)

    actual = []
    tree.inOrderTraverse(tree.root, lambda node: actual.append(node.key))

    expected = [2, 5, 9, 12, 13, 15, 17, 18, 19]
    print(actual)
    assert actual == expected



def test_PostOrderTraverse():
    tree = Tree()

    input = [12, 5, 2, 9, 18, 15, 13, 17, 19]
    for each in input:
        tree.insert(each)

    actual = []
    tree.postOrderTraverse(tree.root, lambda node: actual.append(node.key))

    expected = [2, 9, 5, 13, 17, 15, 19, 18, 12]
    print(actual)
    assert actual == expected



def test_LevelOrderTraverse():
    tree = Tree()

    input = [12, 5, 2, 9, 18, 15, 13, 17, 19]
    for each in input:
        tree.insert(each)

    actual = []
    tree.levelOrderTraverse(tree.root, lambda node: actual.append(node.key))

    expected = [12, 5, 18, 2, 9, 15, 19, 13, 17]
    print(actual)
    assert actual == expected

