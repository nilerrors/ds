class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class MyQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        """
        naam: isEmpty
        parameters: geen
        beschrijving: geeft True terug als de queue leeg is, anders False
        output: (isEmtpy: boolean)
        preconditie: geen
        postconditie: geen
        """
        return self.front is None

    def getFront(self):
        """
        naam: getFront
        parameters: geen
        beschrijving: geeft de waarde van de front terug, en als de queue leeg is, wordt None teruggegeven
        output: (front: waarde, isEmtpy: boolean)
        preconditie: geen
        postconditie: geen
        """
        if self.isEmpty():
            return None, False
        return self.front.data, True

    def dequeue(self):
        """
        naam: dequeue
        parameters: geen
        beschrijving: haalt de front uit de queue en geeft de waarde terug, en als de queue leeg is, wordt None teruggegeven
        output: (front: waarde, isEmtpy: boolean)
        preconditie: geen
        postconditie: de queue bevat een waarde minder
        """
        if self.isEmpty():
            return None, False

        if self.front.next is None:
            node = self.front
            self.front = None
            return node.data, True

        node = self.front
        self.front = self.front.next
        return node.data, True

    def enqueue(self, value):
        """
        naam: enqueue
        parameters: (value: waarde)
        beschrijving: voegt een waarde toe aan de queue
        output: (toegevoegd: boolean)
        preconditie: geen
        postconditie: queue bevat een nieuwe waarde
        """
        if self.front is None:
            self.front = Node(value)
            return True
        node = self.front
        while node.next is not None:
            node = node.next
            if node.next is None:
                break
        node.next = Node(value)
        return True

    def load(self, arr):
        """
        naam: load
        parameters: (arr: array)
        beschrijving: laadt een array in de queue
        output: geen
        preconditie: geen
        postconditie: de queue bevat de waarden uit de array
        """
        self.front = None
        arr.reverse()
        for n in arr:
            self.enqueue(n)

    def save(self):
        """
        naam: save
        parameters: geen
        beschrijving: geeft een array terug met de waarden uit de queue
        output: (arr: array)
        preconditie: geen
        postconditie: geen
        """
        arr = []
        node = self.front
        while node is not None:
            arr.append(node.data)
            node = node.next
            if node is None:
                break
        arr.reverse()
        return arr


if __name__ == "__main__":
    q = MyQueue()
    print(q.isEmpty())
    print(q.getFront()[1])
    print(q.dequeue()[1])
    print(q.enqueue(2))
    print(q.enqueue(4))
    print(q.isEmpty())
    print(q.dequeue()[0])
    q.enqueue(5)
    print(q.save())

    q.load(["a", "b", "c"])
    print(q.save())
    print(q.dequeue()[0])
    print(q.save())
    print(q.getFront()[0])
    print(q.save())
