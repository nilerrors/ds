class MyQueue:
    def __init__(self, max_len: int):
        self.items = [None] * max_len

    @property
    def front(self) -> int:
        """
        naam: front
        parameters: geen
        beschrijving: geeft de index van de front terug, en als de queue leeg is, wordt None teruggegeven
        output: (front: index, isEmtpy: boolean)
        preconditie: geen
        postconditie: geen
        """
        if self.isEmpty():
            return None
        return len(self.items) - 1

    def getFront(self):
        """
        naam: getFront
        parameters: geen
        beschrijving: geeft de waarde van de front terug, en als de queue leeg is, wordt None teruggegeven
        output: (front: waarde, isEmtpy: boolean)
        preconditie: geen
        postconditie: geen
        """
        if self.front is None:
            return None, False
        return self.items[self.front], True

    def isEmpty(self) -> bool:
        """
        naam: isEmpty
        parameters: geen
        beschrijving: geeft True terug als de queue leeg is, anders False
        output: (isEmtpy: boolean)
        preconditie: geen
        postconditie: geen
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        naam: enqueue
        parameters: (item: waarde)
        beschrijving: voegt een waarde toe aan de queue
        output: (isEnqueued: boolean)
        preconditie: geen
        postconditie: de queue bevat een waarde meer
        """
        self.items.reverse()
        self.items.append(item)
        self.items.reverse()
        return True

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
        return self.items.pop(), True

    def save(self):
        """
        naam: save
        parameters: geen
        beschrijving: geeft de queue terug
        output: (queue: array)
        preconditie: geen
        postconditie: geen
        """
        return self.items

    def load(self, new_items):
        """
        naam: load
        parameters: (new_items: array)
        beschrijving: laadt een array in de queue
        output: geen
        preconditie: geen
        postconditie: de queue bevat de waarden uit de array
        """
        self.items = new_items
        
