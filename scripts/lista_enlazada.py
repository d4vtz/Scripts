class Iterator:
    def __init__(self, current: str) -> None:
        self.current = current

    def __next__(self):
        if self.current is None:
            raise StopIteration("No hay elementos en la lista")
        else:
            element: str = self.current.element
            self.current = self.current.next
        return element


class Node:
    def __init__(self, element: str) -> None:
        self.element = element
        self.next = None

    def __str__(self) -> str:
        return self.element


class CircularList:
    def __init__(self, string: str) -> None:
        self.initial = None
        self.last = None
        self.len = 0
        self.string = string

        for _ in self.string:
            self.append(_)

    def __len__(self):
        return self.len

    def __iter__(self):
        return Iterator(self.initial)

    def append(self, element: Node) -> Node:
        node = Node(element)
        if self.initial is None:
            self.initial = self.last = node
            self.last.next = self.initial
        else:
            last = self.last
            self.last = last.next = node
            node.next = self.initial
        self.len += 1
        return node


if __name__ == "__main__":
    string = "Hola mundo! "
    link = CircularList(string)
    iterator = iter(link)
    contador = 0
    cadena = ""
    while True:
        for i in range(len(string)):
            cadena += next(iterator)
        contador += 1
