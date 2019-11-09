import csv


class Node:
    def __init__(self, key, value=None, left=None, right=None):
        """

        Parameters
        ----------
            key: the key of the node
            value: the value of the key
        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value=None):
    """
    Inserts a node into the tree. Works down from the root.

    """
    if key < root.key:
        if root.left is None:
            root.left = Node(key, value)
        else:
            insert(root.left, key, value)
    else:
        if root.right is None:
            root.right = Node(key, value)
        else:
            insert(root.right, key, value)
    return root


def search(root, key):
    """
    Locates a node with specified key
    Parameters
    ----------
        root: root of tree
        key: the key of the node
    Returns
    -------
        The node with specified key
    """
    if key == root.key:
        return root.value
    elif key < root.key:
        if root.left is None:
            print('key is not in tree')
            return None
        else:
            return search(root.left, key)
    else:
        if root.right is None:
            print('key not found')
            return None
        else:
            return search(root.right, key)


def create_tree(datafile):
    """
    creates a binary search tree from data
    """

    file = datafile

    isfirstline = True
    for line in open(file, 'r'):
        data = line.rstrip().split('\t')
        if isfirstline is True:
            datatree = Node(data[0], data[1])
            isfirstline = False
        else:
            insert(datatree, data[0], data[1])

    return datatree
