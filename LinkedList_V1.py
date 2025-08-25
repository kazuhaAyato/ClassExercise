# WTF?

class LinkedList_V1:
    def __init__(self):
        self.FreePointers = []
        self.Elements = []
        self.Pointers = []
        self.Start = 0
        self.End = 0
    def add_element(self,element):
        p = 0
        if len(self.FreePointers) > 0:
            p = self.FreePointers.pop()
            self.Elements[p] = element
        else:
            p = len(self.Elements)+1
            self.Elements.append(element)
        self.Pointers.append(-1)
        self.Pointers[self.End] = p
        self.End = p
        return p
    def remove_element(self,element):
        lastposition,position = self.search_element(element)
        if position is None:
            print("Error: NOT FOUND")
            return
        self.Pointers[lastposition] = self.Pointers[position]
        self.FreePointers.append(position)
        if position == self.Start:
            self.Start = self.Pointers[position]
    def search_element(self,element):
        f = False
        last = self.Start
        loopA= self.Start
        while not f:
            if self.Elements[loopA] == element:
                return last,loopA
            else:
                if self.End == loopA:
                    return None
                last = loopA
                loopA = self.Pointers[loopA]
    def output(self):
        n = 0
        s = self.Start
        while True:
            n+=1
            print(f"Node{n}: Position = {s}, Content = {self.Elements[s]}, Next = {self.Pointers[s]}")
            s = self.Pointers[s]
            if s == self.End:
                return
class 
#test
linkedlist = LinkedList_V1()
while True:
    cmd = input("Please Input")
    match cmd:
        case "a":
            a = input("Append What")
            print(f"OK, Added At Position{linkedlist.add_element(a)}")
        case "d":
            d = input("Delete What")
            print("Trying to Remove ELEMENT" + d)
            linkedlist.remove_element(d)
        case "p":
            linkedlist.output()
        case "s":
            s = input("Search What")
            print(linkedlist.search_element(s))
