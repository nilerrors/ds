"""
Node:
 Structure:
       <-(prev: Node | None),(data: Any),(next: Node|None)->

LinkedChain:
 Structure:
                                 head
       <-(prev: Node | None),(data: Any),(next: Node|None)->
                                 tail
       <-(prev: Node | None),(data: Any),(next: Node|None)->

 Example:
                               head
         tail<-(prev: Node),(data: 3),(next: Node)->tail
                               tail
         head<-(prev: Node),(data: 4),(next: Node)->head

 Methods:
       getLength					: int
           count from head to tail

       isEmpty						: bool
           is length 0

       retrieve(index)				: Tuple[Union[Node, None], False]
           None, False if empty
           node, True if found
           None, False if not found

       insert(index, data)			: bool
           False if empty
           False if not in range
           True if inserted

       delete(index)				: bool
           False if empty
           False if not found
           True if deleted

       save()						: str
           string representation of list
       
       load(arr)					: None
           load into list all from arr (Uses LinkedChain.insert under the hood)


"""


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __repr__(self):
        return f"{self.data}"


class LinkedChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLength(self):
        """
        naam: getLength
        parameters: geen
        beschrijving: geeft de lengte van de lijst terug
        output: (lengte: int)
        preconditie: geen
        postconditie: geen
        """
        _len = 0
        node = self.head
        while node is not None:
            _len += 1
            node = node.next
            if node == self.head:
                break
        return _len

    def isEmpty(self):
        """
        naam: isEmpty
        parameters: geen
        beschrijving: geeft True terug als de lijst leeg is, anders False
        output: (leeg: bool)
        preconditie: geen
        postconditie: geen
        """
        return self.getLength() == 0

    def retrieve(self, index):
        """
        naam: retrieve
        parameters: (index: int)
        beschrijving: geeft de node terug op de gegeven index, als deze bestaat, anders None
        output: (node: Node of None, gevonden: bool)
        preconditie: geen
        postconditie: geen
        """
        if self.isEmpty():
            return None, False
        _len = 0
        node = self.head
        while node is not None:
            _len += 1
            if _len == index:
                return node, True
            node = node.next
            if node == self.head:
                break
        return None, False

    def insert(self, index, data):
        """
        naam: insert
        parameters: (index: int, data: Any)
        beschrijving: voegt een node toe op de gegeven index
        output: (toegevoegd: bool)
        preconditie: geen
        postconditie: een element meer in de lijst
        """
        index -= 1
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
        return True

    def delete(self, index):
        """
        naam: delete
        parameters: (index: int)
        beschrijving: verwijdert de node op de gegeven index
        output: (verwijderd: bool)
        preconditie: geen
        postconditie: een element minder in de lijst
        """
        index -= 1
        if not 0 <= index < self.getLength():
            return False
        if self.head is None or self.tail is None:
            return False
        if self.head == self.tail:
            self.clear()
        elif index == 0:
            if self.tail.next is None:
                return False
            self.tail.next = self.tail.next.next
            self.head = self.head.next
            self.tail.next = self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                if temp is None:
                    return False
                temp = temp.next
            if temp is None or temp.next is None:
                return False
            temp.next, temp.prev = temp.next.next, temp
            if temp is self.tail:
                self.tail = temp
        return True

    def clear(self):
        """
        naam: clear
        parameters: geen
        beschrijving: is private, maakt de lijst leeg
        output: geen
        preconditie: geen
        postconditie: lijst is leeg
        """
        self.head = None
        self.tail = None

    def save(self):
        """
        naam: save
        parameters: geen
        beschrijving: geeft een list representatie van de lijst terug
        output: (list: str)
        preconditie: geen
        postconditie: geen
        """
        items = []
        if self.isEmpty():
            return []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
            if node == self.head:
                break
        return items

    def load(self, arr):
        """
        naam: load
        parameters: (arr: list)
        beschrijving: maakt de lijst leeg en laadt de lijst met de gegeven list
        output: geen
        preconditie: geen
        postconditie: lijst is geladen met de gegeven list
        """
        self.clear()
        for i, n in enumerate(arr):
            self.insert(i + 1, n)


if __name__ == "__main__":
    l = LinkedChain()
    print(l.isEmpty())
    print(l.getLength())
    print(l.retrieve(4)[1])
    print(l.insert(4, 500))
    print(l.isEmpty())
    print(l.insert(1, 500))
    print(l.retrieve(1)[0])
    print(l.retrieve(1)[1])
    print(l.save())
    print(l.insert(1, 600))
    print(l.save())
    l.load([10, -9, 15])
    l.insert(3, 20)
    print(l.delete(0))
    print(l.save())
    print(l.delete(1))
    print(l.save())
