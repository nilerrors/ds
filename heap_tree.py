DEBUG = False


def log(*items, enter=False, sep=" ", end="\n"):
    """
    naam: log
    parameters: (items: list, enter: boolean, sep: string, end: string)
    beschrijving: print de items op het scherm als DEBUG True is; alleen voor debugging
    output: geen
    preconditie: geen
    postconditie: geen
    """
    if not DEBUG:
        return
    if enter:
        print()
        return
    print("DEBUG:", *items, sep=sep, end=end)


class Node:
    def __init__(self, key):
        self.key = key
        self.parent: Node | None = None
        self.left: Node | None = None
        self.right: Node | None = None
        self.is_left_child = True

    def is_leaf(self):
        """
        naam: is_leaf
        parameters: geen
        beschrijving: geeft True terug als de node een blad is, anders False
        output: (is_leaf: boolean)
        preconditie: geen
        postconditie: geen
        """
        return self.left is None and self.right is None


class Heap:
    def __init__(self, maxHeap=True):
        self.maxHeap = maxHeap
        self.root = None

    def __height(self, node: Node | None):
        """
        naam: __height
        parameters: (node: Node)
        beschrijving: geeft de hoogte van de node terug
        output: (height: integer)
        preconditie: geen
        postconditie: geen
        """
        if node is None:
            return 0

        return 1 + max(self.__height(node.left), self.__height(node.right))

    def __nodes(self, node: Node | None):
        """
        naam: __nodes
        parameters: (node: Node)
        beschrijving: geeft het aantal nodes in de (deel)boom terug
        output: (nodes: integer)
        preconditie: geen
        postconditie: geen
        """
        if node is None:
            return 0

        return 1 + self.__nodes(node.left) + self.__nodes(node.right)

    def last_node(self):
        """
        naam: last_node
        parameters: geen
        beschrijving: geeft de laatste node van de heap-boom terug
        output: (last_node: Node)
        preconditie: geen
        postconditie: geen
        """
        if self.root is None:
            return None

        def last(node: Node | None):
            if node is None or node.is_leaf():
                return node
            if self.__height(node.left) > self.__height(node.right):
                return last(node.left)
            return last(node.right)

        return last(self.root)

    def heapIsEmpty(self):
        """
        naam: heapIsEmpty
        parameters: geen
        beschrijving: geeft True terug als de heap leeg is, anders False
        output: (heapIsEmpty: boolean)
        preconditie: geen
        postconditie: geen
        """
        return self.root is None

    def heapDelete(self):
        """
        naam: heapDelete
        parameters: geen
        beschrijving: verwijdert de root van de heap en geeft de waarde terug, en als de heap leeg is, wordt None teruggegeven
        output: (root: waarde, deleted: boolean)
        preconditie: geen
        postconditie: de heap bevat een node minder
        """
        if self.root is None:
            return None, False
        if self.root.is_leaf():
            key = self.root.key
            self.root = None
            return key, True

        node = self.last_node()

        if node is None or node.parent is None:
            return None, False

        self.swap(self.root, node)
        # remove last element
        key = node.key
        log("tree:", self.save())
        log("delete node:", node.key)
        log("node parent:", None if node.parent is None else node.parent.key)

        if node.is_left_child:
            node.parent.left = None
        else:
            node.parent.right = None

        self.rebuild(self.root)
        return key, True

    def rebuild(self, node: Node | None):
        """
        naam: rebuild
        parameters: (node: Node)
        beschrijving: herstelt de heap-eigenschap van de heap-boom
        output: geen
        preconditie: geen
        postconditie: de boom is een heap
        """
        if node is None or node.left is None:
            return None

        if self.maxHeap:
            if node.left.key > node.key:
                self.swap(node, node.left)
                self.rebuild(node.left)
                if node.right is not None and node.right.key > node.key:
                    self.swap(node, node.right)
                    self.rebuild(node.right)
        else:
            if node.left.key < node.key:
                self.swap(node, node.left)
                self.rebuild(node.left)
                if node.right is not None and node.right.key < node.key:
                    self.swap(node, node.right)
                    self.rebuild(node.right)

    def insert(self, node: Node, item: int):
        """
        naam: insert
        parameters: (node: Node, item: waarde)
        beschrijving: voegt een waarde toe aan de heap-boom
        output: (node: Node, inserted: boolean)
        preconditie: de node mag niet leeg zijn
        postconditie: de boom bevat een nieuwe waarde
        """
        if node.left is None:
            node.left = Node(item)
            node.left.parent = node
            node.left.is_left_child = True
            return node.left, True
        elif node.right is None:
            node.right = Node(item)
            node.right.parent = node
            node.right.is_left_child = False
            return node.right, True
        elif self.__nodes(node.left) % 3 == 0 and self.__nodes(
            node.left
        ) != self.__nodes(node.right):
            return self.insert(node.right, item)
        else:
            return self.insert(node.left, item)

    def heapInsert(self, item):
        """
        naam: heapInsert
        parameters: (item: waarde)
        beschrijving: voegt een waarde toe aan de heap-boom, en als de heap leeg is, wordt de waarde de root
        output: (inserted: boolean)
        preconditie: geen
        postconditie: de boom bevat een nieuwe waarde
        """
        if self.root is None:
            log("inserted at root:", item)
            self.root = Node(item)
            return True

        node, inserted = self.insert(self.root, item)
        log(self.save())

        if not inserted:
            log("not inserted", item)
            return False

        log("node at end:", node.key)
        log("node parent:", None if node.parent is None else node.parent.key)

        while node is not self.root and node.parent is not None:
            parent = node.parent
            if self.maxHeap and parent.key < node.key:
                self.swap(parent, node)
                node = parent
            elif not self.maxHeap and parent.key > node.key:
                self.swap(parent, node)
                node = parent
            else:
                break

        return True

    def swap(self, node1: Node, node2: Node):
        """
        naam: swap
        parameters: (node1: Node, node2: Node)
        beschrijving: verwisselt de waarden van twee nodes
        output: geen
        preconditie: de nodes mogen niet None zijn
        postconditie: de nodes hebben van waarde gewisseld
        """
        node1.key, node2.key = node2.key, node1.key

    def save(self):
        """
        naam: save
        parameters: geen
        beschrijving: geeft de heap-boom terug als een dictionary
        output: (tree: dictionary)
        preconditie: geen
        postconditie: geen
        """
        if self.heapIsEmpty():
            return None

        def as_dict(node: Node | None):
            if node is None:
                return None
            _dict = {
                "root": node.key,
            }
            if not node.is_leaf():
                _dict["children"] = [as_dict(node.left), as_dict(node.right)]
            return _dict

        return as_dict(self.root)

    def __load(self, tree, is_root=False):
        """
        naam: __load
        parameters: (tree: dictionary, is_root: boolean)
        beschrijving: laadt een dictionary in de heap-boom
        output: (node: Node)
        preconditie: geen
        postconditie: de boom bevat de waarden uit de dictionary
        """
        if tree is not None:
            key = tree["root"]
            node = Node(key)
            if tree.get("children") is not None:
                node.left = self.__load(tree["children"][0])
                if node.left is not None:
                    node.left.parent = node
                    node.left.is_left_child = True
                node.right = self.__load(tree["children"][1])
                if node.right is not None:
                    node.right.parent = node
                    node.right.is_left_child = False

            if is_root:
                self.root = node

            return node

    def load(self, tree):
        """
        naam: load
        parameters: (tree: dictionary)
        beschrijving: maakt de heap-boom eerst leeg en laadt een dictionary in de heap-boom
        output: geen
        preconditie: geen
        postconditie: de boom bevat de waarden uit de dictionary
        """
        self.root = None
        self.__load(tree, True)


if __name__ == "__main__":
    t = Heap()
    t.heapInsert(5)
    expected = {
        "root": 5,
    }
    assert (
        t.save() == expected
    ), f"test 0, insert failed\ngot:      {t.save()}\nexpected: {expected}"
    t.heapInsert(8)
    expected = {
        "root": 8,
        "children": [
            {"root": 5},
            None,
        ],
    }
    assert (
        t.save() == expected
    ), f"test 0, insert failed\ngot:      {t.save()}\nexpected: {expected}"
    t.heapInsert(10)
    expected = {
        "root": 10,
        "children": [
            {"root": 5},
            {"root": 8},
        ],
    }
    assert (
        t.save() == expected
    ), f"test 0, insert failed\ngot:      {t.save()}\nexpected: {expected}"
    t.heapInsert(4)
    expected = {
        "root": 10,
        "children": [
            {"root": 5, "children": [{"root": 4}, None]},
            {"root": 8},
        ],
    }
    assert (
        t.save() == expected
    ), f"test 0, insert failed\ngot:      {t.save()}\nexpected: {expected}"
    t.heapInsert(3)
    expected = {
        "root": 10,
        "children": [
            {"root": 5, "children": [{"root": 4}, {"root": 3}]},
            {"root": 8},
        ],
    }
    assert (
        t.save() == expected
    ), f"test 0, insert failed\ngot:      {t.save()}\nexpected: {expected}"
    log("test starts")
    t.heapInsert(7)
    expected = {
        "root": 10,
        "children": [
            {"root": 5, "children": [{"root": 4}, {"root": 3}]},
            {"root": 8, "children": [{"root": 7}, None]},
        ],
    }
    assert (
        t.save() == expected
    ), f"test 0, insert failed\ngot:      {t.save()}\nexpected: {expected}"


if __name__ == "__main__":
    # Test 1
    log("test 1")
    t = Heap()
    assert t.heapIsEmpty()
    assert not t.heapDelete()[1]
    assert t.heapInsert(5)
    assert t.heapInsert(8)
    assert not t.heapIsEmpty()
    expected = {
        "root": 8,
        "children": [{"root": 5}, None],
    }
    assert (
        t.save() == expected
    ), f"test 1, insert failed\ngot:      {t.save()}\nexpected: {expected}"
    t.load({"root": 10, "children": [{"root": 5}, None]})
    assert t.heapInsert(15)
    expected = {"root": 15, "children": [{"root": 5}, {"root": 10}]}
    assert (
        t.save() == expected
    ), f"test 1, insert after load failed\ngot:      {t.save()}\nexpected: {expected}"
    result = t.heapDelete()
    assert result[0] == 15
    assert result[1]
    expected = {"root": 10, "children": [{"root": 5}, None]}
    assert (
        t.save() == expected
    ), f"test 1, delete after load and insert failed\ngot:      {t.save()}\nexpected: {expected}"


if __name__ == "__main__":
    # Test 2
    log(enter=True)
    log("test 2")
    t = Heap()
    t.heapInsert(2)
    t.heapInsert(3)
    t.heapInsert(1)
    t.heapInsert(5)
    t.heapInsert(9)
    expected = {
        "root": 9,
        "children": [{"root": 5, "children": [{"root": 2}, {"root": 3}]}, {"root": 1}],
    }
    assert (
        t.save() == expected
    ), f"test 2 failed, insert:\ngot:      {t.save()}\nexpected: {expected}"


if __name__ == "__main__":
    # Test 3
    log(enter=True)
    log("test 3")
    t = Heap()
    t.load(
        {
            "root": 9,
            "children": [
                {"root": 5, "children": [{"root": 2}, {"root": 3}]},
                {"root": 1},
            ],
        }
    )
    expected = {
        "root": 9,
        "children": [
            {"root": 5, "children": [{"root": 2}, {"root": 3}]},
            {"root": 1},
        ],
    }
    assert (
        t.save() == expected
    ), f"value not loaded correctly\ngot:      {t.save()}\nexpected: {expected}"
    result = t.heapDelete()
    result = t.heapDelete()
    expected = {
        "root": 3,
        "children": [{"root": 2}, {"root": 1}],
    }
    assert (
        t.save() == expected
    ), f"test 3 failed, delete\ngot:      {t.save()}\nexpected: {expected}"


if __name__ == "__main__":
    # Test 4
    log(enter=True)
    log("test 4")
    t = Heap()
    t.load({"root": 3, "children": [{"root": 2}, {"root": 1}]})
    expected = {
        "root": 3,
        "children": [{"root": 2}, {"root": 1}],
    }
    assert (
        t.save() == expected
    ), f"value not loaded correctly\ngot:      {t.save()}\nexpected: {expected}"
    assert t.heapInsert(5)
    assert t.heapInsert(4)
    result = t.heapDelete()
    expected = {
        "root": 4,
        "children": [{"root": 3, "children": [{"root": 2}, None]}, {"root": 1}],
    }
    assert (
        t.save() == expected
    ), f"test 4 failed, insert and delete\ngot:      {t.save()}\nexpected: {expected}"


if __name__ == "__main__":
    t = Heap()
    for i in range(1, 11):
        t.heapInsert(i)
    expected = {
        "root": 10,
        "children": [
            {
                "root": 9,
                "children": [
                    {"root": 7, "children": [{"root": 1}, {"root": 4}]},
                    {"root": 8, "children": [{"root": 3}, None]},
                ],
            },
            {"root": 6, "children": [{"root": 2}, {"root": 5}]},
        ],
    }
    assert (
        t.save() == expected
    ), f"test 0, insert failed\ngot:      {t.save()}\nexpected: {expected}"
