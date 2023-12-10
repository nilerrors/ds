class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __eq__(self, __value: "Node"):
        if hasattr(__value, "data"):
            return self.data == __value.data
        return self.data == __value

    def __gt__(self, __value: "Node"):
        return self.data > __value.data

    def __repr__(self):
        return f"{self.data}"


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__len = 0

    def getLength(self):
        return len(self)

    def __len__(self):
        return self.__len

    def isEmpty(self):
        return len(self) == 0

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __getitem__(self, index):
        if len(self) == 0:
            raise ValueError(f"List is empty")
        if index < 0 or index > self.getLength():
            raise IndexError(f"index, {index}, out of range")
        node, found = self.retrieve(index)
        if not found or node is None:
            raise KeyError(f"not found at index {index}")
        return node

    def swap(self, index1, index2):
        if index1 < 0 or index1 > self.getLength():
            raise IndexError(f"index, {index1}, out of range")
        if index1 < 0 or index2 > self.getLength():
            raise IndexError(f"index, {index2}, out of range")

        self[index1].data, self[index2].data = self[index2].data, self[index1].data

    def retrieve(self, index):
        if self.isEmpty():
            return None, False
        _len = 0
        node = self.head
        while node is not None:
            if _len == index:
                return node, True
            _len += 1
            node = node.next
            if node == self.head:
                break
        if _len == index:
            return node, True
        return None, False

    def append(self, data):
        return self.insert(len(self), data)

    def insert(self, index, data):
        if index < 0 or index > self.getLength():
            return False
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.tail = new_node
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            if self.tail is None:
                return False
            self.head = new_node
            self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                if temp is None:
                    return False
                temp = temp.next
            if temp is None:
                return False
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node
            if temp is self.tail:
                self.tail = new_node
                self.head.prev = self.tail
        self.__len += 1
        return True

    def pop(self):
        return self.delete(len(self))

    def delete(self, index):
        if index < 0 or index > self.getLength():
            return None, False
        if self.head is None or self.tail is None:
            return None, False
        deleted_node = self.head
        if self.head == self.tail:
            self.clear()
        elif index == 0:
            if self.tail.next is None:
                return None, False
            self.tail.next = self.tail.next.next
            self.head = self.head.next
            self.tail.next = self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                if temp is None:
                    return None, False
                temp = temp.next
            if temp is None or temp.next is None:
                return None, False
            deleted_node = temp
            temp.next, temp.prev = temp.next.next, temp
            if temp is self.tail:
                self.tail = temp
        self.__len -= 1
        return deleted_node, True

    def clear(self):
        self.head = None
        self.tail = None

    def save(self):
        return list(self)

    def __repr__(self) -> str:
        return repr(self.save())

    def load(self, arr):
        self.clear()
        for i, n in enumerate(arr):
            self.insert(i + 1, n)

    def copy(self):
        new_list = List()
        new_list.load(self.save())
        return new_list


class Heap:
    def __init__(self, maxHeap=True):
        self.maxHeap = maxHeap
        self._heap = List()

    def clear(self):
        self._heap = List()

    def heapIsEmpty(self):
        return self._heap.isEmpty()

    def heapDelete(self):
        if len(self._heap) == 0:
            return None, False
        self.swap(0, len(self._heap) - 1)
        item, deleted = self._heap.pop()
        self.rebuild()

        return item, deleted

    def heapInsert(self, item):
        self._heap.append(item)
        index = len(self._heap) - 1

        while index > 0:
            parent_index = self.parent(index)
            if self.maxHeap and self._heap[parent_index] < self._heap[index]:
                index, _ = self.swap(index, parent_index)
            elif not self.maxHeap and self._heap[parent_index] > self._heap[index]:
                index, _ = self.swap(index, parent_index)
            else:
                break

        return True

    def sort(self):
        unsorted = self._heap.copy()
        for i in range(self.size // 2)[::-1]:
            self.rebuild(i)
        last = self.size - 1
        for i in range(self.size):
            self.swap(0, last)
            last -= 1
            self.rebuild(0, last + 1)
        return unsorted

    def rebuild(self, root=0, size=None):
        if size is None:
            size = self.size

        while True:
            left_child = self.left_child(root)
            right_child = self.right_child(root)
            child = root

            if self.maxHeap:
                if left_child < size and self._heap[left_child] > self._heap[child]:
                    child = left_child
                if right_child < size and self._heap[right_child] > self._heap[child]:
                    child = right_child
            else:
                if left_child < size and self._heap[left_child] < self._heap[child]:
                    child = left_child
                if right_child < size and self._heap[right_child] < self._heap[child]:
                    child = right_child

            if child != root:
                self.swap(root, child)
                root = child
            else:
                break

    def swap(self, index1, index2):
        self._heap.swap(index1, index2)
        return index2, index1

    def is_leaf(self, index: int = 0, size=None):
        if size is None:
            size = self.size
        return size <= index * 2 + 1

    def has_right_child(self, index: int = 0, size=None):
        if size is None:
            size = self.size
        return size > index * 2 + 2

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index=0):
        return index * 2 + 1

    def right_child(self, index=0):
        return index * 2 + 2

    @property
    def size(self) -> int:
        return len(self)

    def __len__(self) -> int:
        return len(self._heap)

    def __str__(self) -> str:
        return str(self._heap)

    def save(self):
        if self.heapIsEmpty():
            return None

        def heap_node(index):
            if index is None:
                return None
            if index >= len(self._heap):
                return None

            _dict = {"root": self._heap[index].data}
            if not self.is_leaf(index):
                _dict["children"] = [
                    heap_node(self.left_child(index)),
                    heap_node(self.right_child(index)),
                ]
            return _dict

        return heap_node(0)

    def __load(self, index, tree, exclude_self=False):
        if index is not None and tree is not None:
            if not exclude_self:
                self._heap.append(tree["root"])
            if tree.get("children") is not None:
                left_child = tree["children"][0]
                right_child = tree["children"][1]
                if left_child is not None:
                    self._heap.append(left_child["root"])
                if right_child is not None:
                    self._heap.append(right_child["root"])
                if left_child is not None:
                    self.__load(self.left_child(index), left_child, exclude_self=True)
                if right_child is not None:
                    self.__load(self.right_child(index), right_child, exclude_self=True)
            self.rebuild()

    def load(self, tree):
        self.clear()
        self.__load(0, tree)

    def __repr__(self):
        return repr(self.save())


if __name__ == "__main__":
    # True
    # False
    # True
    # True
    # False
    # {'root': 8,'children':[{'root':5},None]}
    # {'root': 15,'children':[{'root':5},{'root':10}]}
    # 15
    # True
    # {'root': 10,'children':[{'root':5},None]}
    t = Heap()
    assert t.heapIsEmpty()
    assert not t.heapDelete()[1]
    assert t.heapInsert(5)
    assert t.heapInsert(8)
    assert not t.heapIsEmpty()
    assert t.save() == {"root": 8, "children": [{"root": 5}, None]}
    t.load({"root": 10, "children": [{"root": 5}, None]})
    assert t.heapInsert(15)
    assert t.save() == {"root": 15, "children": [{"root": 5}, {"root": 10}]}
    result = t.heapDelete()
    assert result[0] == 15
    assert result[1]
    assert t.save() == {"root": 10, "children": [{"root": 5}, None]}


if __name__ == "__main__":
    # {'root': 9, 'children': [{'root': 5, 'children': [{'root': 2}, {'root': 3}]}, {'root': 1}]}
    t = Heap()
    t.heapInsert(2)
    t.heapInsert(3)
    t.heapInsert(1)
    t.heapInsert(5)
    t.heapInsert(9)
    assert t.save() == {
        "root": 9,
        "children": [{"root": 5, "children": [{"root": 2}, {"root": 3}]}, {"root": 1}],
    }, "test 2 failed, insert"


if __name__ == "__main__":
    # {'root': 3, 'children': [{'root': 2}, {'root': 1}]}
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
    assert t.save() == {
        "root": 9,
        "children": [
            {"root": 5, "children": [{"root": 2}, {"root": 3}]},
            {"root": 1},
        ],
    }, "value not loaded correctly"
    result = t.heapDelete()
    result = t.heapDelete()
    assert t.save() == {
        "root": 3,
        "children": [{"root": 2}, {"root": 1}],
    }, "test 3 failed, delete"


if __name__ == "__main__":
    # {'root': 4, 'children': [{'root': 3, 'children': [{'root': 2}, None]}, {'root': 1}]}
    t = Heap()
    t.load({"root": 3, "children": [{"root": 2}, {"root": 1}]})
    assert t.save() == {
        "root": 3,
        "children": [{"root": 2}, {"root": 1}],
    }, "value not loaded correctly"
    assert t.heapInsert(5)
    assert t.heapInsert(4)
    result = t.heapDelete()
    assert t.save() == {
        "root": 4,
        "children": [{"root": 3, "children": [{"root": 2}, None]}, {"root": 1}],
    }, "test 4 failed, insert and delete"


print("all tests passed successfully")
