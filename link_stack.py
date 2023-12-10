class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class MyStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        """
        naam: isEmpty
        parameters: geen
        beschrijving: geeft True terug als de stack leeg is, anders False
        output: (isEmtpy: boolean)
        postconditie: geen
        preconditie: geen
        """
        return self.top is None

    def getTop(self):
        """
        naam: getTop
        parameters: geen
        beschrijving: geeft de waarde van de top terug, en als de stack leeg is, wordt None teruggegeven
        output: (top: waarde, bestaat: boolean)
        postconditie: geen
        preconditie: geen
        """
        if self.isEmpty():
            return None, False
        return self.top.data, True

    def pop(self):
        """
        naam: pop
        parameters: geen
        beschrijving: verwijdert de top van de stack en geeft de waarde terug, en als de stack leeg is, wordt None teruggegeven
        output: (top: waarde, verwijderd: boolean)
        preconditie: geen
        postconditie: de top is verwijderd
        """
        if self.isEmpty():
            return None, False
        top = self.top
        self.top = self.top.next

        return top.data, True

    def push(self, value):
        """
        naam: push
        parameters: (value: waarde)
        beschrijving: voegt een waarde toe aan de top van de stack
        output: (toegevoegd: boolean)
        preconditie: geen
        postconditie: de waarde is toegevoegd aan de top van de stack
        """
        self.top = Node(value, self.top)
        return True

    def load(self, arr):
        """
        naam: load
        parameters: (arr: array)
        beschrijving: laadt een array in de stack
        output: geen
        preconditie: geen
        postconditie: de stack bevat de waarden uit de array
        """
        self.top = None
        for n in arr:
            self.top = Node(n, self.top)

    def save(self):
        """
        naam: save
        parameters: geen
        beschrijving: geeft een array terug met de waarden uit de stack
        output: (arr: array)
        preconditie: geen
        postconditie: geen
        """
        arr = []
        node = self.top
        while node is not None:
            arr.append(node.data)
            node = node.next
            if node is None:
                break
        arr.reverse()
        return arr


if __name__ == "__main__":
    s = MyStack()
    print(s.isEmpty())
    print(s.getTop()[1])
    print(s.pop()[1])
    print(s.push(2))
    print(s.push(4))
    print(s.isEmpty())
    print(s.pop()[0])
    s.push(5)
    print(s.save())

    s.load(["a", "b", "c"])
    print(s.save())
    print(s.pop()[0])
    print(s.save())
    print(s.getTop()[0])
    print(s.save())
