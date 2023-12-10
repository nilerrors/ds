"""
Node:
 Structure:
     (key),(data)		: Any
        /	\
    (left) (right)		: Union[Node, None] = None
 
 Example:
       (5),(5)			: int
        /	\
    (None) (None)		: None
    
       is_leaf() -> True
    
 Methods:
       is_leaf					: bool
           has no children

       retrieve(key)			: Tuple[Union[Node, None], bool]
           (None, False) if not found
           (node, True)  if found
       
       insert(new_node)			: bool
           key < self.key:
               insert in left
           key > self.key:
               insert in right

        delete(key)				: Union[Node, None]
            None if not found
            node if found and deleted

        inorder					: List[key]
            inorder links
            key
            inorder right
        
        as_dict 				: Union[{'root': key}, {'root': key, 'children': [left, right]}]
            dictionary representation of Node


BST:
 Structure:
     (root)				: Union[Node, None] = None
 
 Example:
           root
             ↓
          (5),(5)					: int
         /       \
    ((3),(3))  ((6),(6))			: Node
     /    \      /    \
  (None)(None) (None)(None)			: None
 
 Methods:
       isEmpty						: bool
           is root None

       searchTreeInsert(new_node)	: bool
           first item:
               in root
           else:
               insert in root (uses Node.insert)

       searchTreeRetrieve(key)		: Tuple[Union[Node, None], bool]
           retrieve from root (uses Node.retrieve)

       searchTreeDelete(key)		: bool
           False if empty
           False if not found
           True if deleted
       
       inorderTraverse(func)		: None
           func foreach in inorder root
       
       save							: str
           string representation of dictionary representation of
             root node (and all of its children)
             
       load(tree)					: None
           convert given dictionary representation of BST to BST

"""




class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

    def is_leaf(self):
        """
        naam: is_leaf
        parameters: geen
        beschrijving: geeft True terug als de node geen kinderen heeft, anders False
        output: (is_leaf: boolean)
        preconditie: geen
        postconditie: geen
        """
        return self.left is None and self.right is None

    def retrieve(self, key):
        """
        naam: retrieve
        parameters: (key: waarde)
        beschrijving: geeft de node terug met de gegeven key, en als de node niet bestaat, wordt None teruggegeven
        output: (node: Node, gevonden: boolean)
        preconditie: geen
        postconditie: geen
        """
        if self is None:
            return None, False
        if key == self.key:
            return self, True
        if key < self.key:
            if self.left:
                return self.left.retrieve(key)
            return None, False
        if key > self.key:
            if self.right:
                return self.right.retrieve(key)
            return None, False

    def insert(self, new_node: "Node") -> bool:
        """
        naam: insert
        parameters: (new_node: Node)
        beschrijving: voegt een node toe aan de bst
        output: (isInserted: boolean)
        preconditie: geen
        postconditie: de bst bevat een node meer
        """
        if self.key is None:
            self.key = new_node.key
            self.data = new_node.data
            return True

        if new_node.key < self.key:
            if self.left is not None:
                return self.left.insert(new_node)
            self.left = new_node
            return True

        if self.right is not None:
            return self.right.insert(new_node)
        self.right = new_node
        return True

    def delete(self, key):
        """
        naam: delete
        parameters: (key: waarde)
        beschrijving: verwijdert de node met de gegeven key, en als de node niet bestaat, wordt None teruggegeven
        output: (node: Node)
        preconditie: geen
        postconditie: de bst bevat een node minder
        """
        if key < self.key:
            if self.left is not None:
                self.left = self.left.delete(key)
            return self
        elif key > self.key:
            if self.right is not None:
                self.right = self.right.delete(key)
            return self
        else:
            if self.is_leaf():
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                successor = self.right
                while successor.left:
                    successor = successor.left
                self.key, self.data = successor.key, successor.data
                self.right = self.right.delete(successor.key)
                return self

    def inorder(self, arr: list):
        """
        naam: inorder
        parameters: (arr: list)
        beschrijving: voegt elementen toe aan de array in inorder
        output: (arr: list)
        preconditie: geen
        postconditie: geen
        """
        if self.left is not None:
            self.left.inorder(arr)
        if self.key is not None:
            arr.append(self.key)
        if self.right is not None:
            self.right.inorder(arr)
        return arr

    def as_dict(self):
        """
        naam: as_dict
        parameters: geen
        beschrijving: geeft een dictionary terug van de node
        output: (dict: {'root': key} of {'root': key, 'children': [left, right]) 
        preconditie: geen
        """
        _dict = {
            "root": self.key,
        }
        if not self.is_leaf():
            _dict["children"] = [None, None]
            if self.left is not None:
                _dict["children"][0] = self.left.as_dict()
            if self.right is not None:
                _dict["children"][1] = self.right.as_dict()
        return _dict


def createTreeItem(key, data):
    return Node(key, data)


class BST:
    def __init__(self):
        self.root: Node | None = None

    def isEmpty(self):
        """
        naam: isEmpty
        parameters: geen
        beschrijving: geeft True terug als de bst leeg is, anders False
        output: (isEmpty: boolean)
        preconditie: geen
        postconditie: geen
        """
        return self.root is None

    def save(self):
        """
        naam: save
        parameters: geen
        beschrijving: geeft de bst terug
        output: (bst: dictionary)
        preconditie: boom mag niet leeg zijn
        postconditie: geen
        """
        return self.root.as_dict()

    def searchTreeInsert(self, node: Node):
        """
        naam: searchTreeInsert
        parameters: (node: Node)
        beschrijving: voegt een node aan de bst toe
        output: (isInserted: boolean)
        preconditie: geen
        postconditie: de bst bevat een node meer
        """
        if self.isEmpty():
            self.root = node
            return True

        return self.root.insert(node)

    def searchTreeRetrieve(self, key):
        """
        naam: searchTreeRetrieve
        parameters: (key: waarde)
        beschrijving: geeft de node terug met de gegeven key, en als de node niet bestaat, wordt None teruggegeven
        output: (node: Node, gevonden: boolean)
        preconditie: geen
        postconditie: geen
        """
        if self.isEmpty():
            return None, False
        node, found = self.root.retrieve(key)
        if found:
            return node.key, True
        return None, False

    def inorderTraverse(self, func):
        """
        naam: inorderTraverse
        parameters: (func: function)
        beschrijving: voert een functie uit voor elke node in inorder
        output: geen
        preconditie: geen
        postconditie: geen
        """
        if self.isEmpty():
            return
        traverse = []
        self.root.inorder(traverse)
        for key in traverse:
            func(key)

    def __load(self, tree):
        """
        naam: __load
        parameters: (tree: dictionary)
        beschrijving: is prive, zet een dictionary om in een bst
        output: geen
        precondities: geen
        postcondities: de bst bevat alle nodes van de dictionary
        """
        if tree is not None:
            key = tree["root"]
            node = createTreeItem(key, key)
            self.searchTreeInsert(node)
            if tree.get("children") is not None:
                self.__load(tree["children"][0])
                self.__load(tree["children"][1])

    def load(self, tree):
        """
        naam: load
        parameters: (tree: dictionary)
        beschrijving: maakt de boom eerst leeg en zet een dictionary om in een bst
        output: geen
        precondities: geen
        postcondities: de bst bevat alle nodes van de dictionary
        """
        self.root = None
        self.__load(tree)

    def searchTreeDelete(self, key):
        """
        naam: searchTreeDelete
        parameters: (key: waarde)
        beschrijving: verwijdert de node met de gegeven key, en als de node niet bestaat, wordt None teruggegeven
        output: (isDeleted: boolean)
        preconditie: geen
        postconditie: de bst bevat een node minder
        """
        if self.root is None:
            return False

        if self.root.key == key:
            new_root = self.root.delete(key)
            if new_root is not None:
                self.root = new_root
            return new_root is not None

        self.root = self.root.delete(key)
        return self.root is not None


if __name__ == "__main__":
    t = BST()
    print(t.isEmpty())
    print(t.searchTreeInsert(createTreeItem(8, 8)))
    print(t.searchTreeInsert(createTreeItem(5, 5)))
    print(t.isEmpty())
    print(t.searchTreeRetrieve(5)[0])
    print(t.searchTreeRetrieve(5)[1])
    print(t.save())
    t.load({"root": 10, "children": [{"root": 5}, None]})
    t.searchTreeInsert(createTreeItem(15, 15))
    print(t.searchTreeDelete(0))
    print(t.save())
    print(t.searchTreeDelete(10))
    print(t.save())

if __name__ == "__main__":
    t = BST()
    t.load(
        {
            "root": 100,
            "children": [
                {
                    "root": 50,
                    "children": [
                        {"root": 20},
                        {"root": 90, "children": [{"root": 70}, None]},
                    ],
                },
                {"root": 200, "children": [{"root": 120}, {"root": 210}]},
            ],
        }
    )
    t.searchTreeDelete(90)
    t.searchTreeDelete(70)
    t.searchTreeDelete(100)
    print(t.save())


if __name__ == "__main__":
    t = BST()
    t.load(
        {
            "root": 120,
            "children": [
                {"root": 50, "children": [{"root": 20}, None]},
                {"root": 200, "children": [None, {"root": 210}]},
            ],
        }
    )
    t.searchTreeInsert(createTreeItem(110, 110))
    t.searchTreeInsert(createTreeItem(150, 150))
    t.searchTreeDelete(210)
    t.searchTreeDelete(120)
    print(t.save())
