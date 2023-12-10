class MyStack:
    def __init__(self, max_len: int):
        self.items = [None] * max_len

    @property
    def top(self) -> int:
        """
        naam: top
        parameters: geen
        beschrijving: geeft de index van de top terug, en als de stack leeg is, wordt None teruggegeven
        output: (top: index of None)
        postconditie: geen
        preconditie: geen
        """
        if self.isEmpty():
            return None
        return len(self.items) - 1

    def getTop(self):
        """
        naam: getTop
        parameters: geen
        beschrijving: geeft de waarde van de top terug, en als de stack leeg is, wordt None teruggegeven
        output: (top: waarde, bestaat: boolean)
        postconditie: geen
        preconditie: geen
        """
        if self.top is None:
            return None, False
        return self.items[self.top], True

    def isEmpty(self) -> bool:
        """
        naam: isEmpty
        parameters: geen
        beschrijving: geeft True terug als de stack leeg is, anders False
        output: (isEmtpy: boolean)
        postconditie: geen
        preconditie: geen
        """
        return len(self.items) == 0

    def push(self, item):
        """
        naam: push
        parameters: (item: waarde)
        beschrijving: voegt een waarde toe aan de top van de stack
        output: (toegevoegd: boolean)
        preconditie: geen
        postconditie: de waarde is toegevoegd aan de top van de stack
        """
        self.items.append(item)
        return True

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
        return self.items.pop(), True

    def save(self):
        """
        naam: save
        parameters: geen
        beschrijving: geeft een array terug met de waarden uit de stack
        output: (arr: array)
        preconditie: geen
        postconditie: geen
        """
        return self.items

    def load(self, new_items):
        """
        naam: load
        parameters: (arr: array)
        beschrijving: laadt een array in de stack
        output: geen
        preconditie: geen
        postconditie: de stack bevat de waarden uit de array
        """
        self.items = new_items
