#FUCK. I hate PY
import pickle
#👆 Yeah!!!!! I Love This Library


class Node:
    def __init__(self,content,next):
        self.content = content
        self.next = next
    def getNext(self):
        return self.next
    def getContent(self):
        return self.content
    def setPointer(self,pt):
        self.next = pt
class LinkedList_V2:
    def __init__(self, node):
        self.Elements = [node]
        self.TopPointer = 0 #First Element of LinkedList
        self.BtmPointer = 0 #Next Element Position
    def add_element(self,content):
        node_add = Node(content,-1)
        self.Elements[self.BtmPointer].setPointer(self.BtmPointer + 1)
        self.Elements.append(node_add)
        self.BtmPointer +=1
    def remove_element(self,position):
        for i in self.Elements:
            if i.getNext() == position :
                i.setPointer(self.Elements[position].getNext())
                self.Elements[position].pop()
                return
    def insert_element(self,position,ct):
        node = Node(ct,self.Elements[position].getNext())
        self.Elements[position].setPointer(self.BtmPointer + 1)
        self.BtmPointer += 1
        self.Elements.append(node)
    def output(self):
        pointer = self.TopPointer
        while pointer != -1:
            print(f"pointer={pointer},content={self.Elements[pointer].getContent()}, next = {self.Elements[pointer].getNext()}")
            pointer = self.Elements[pointer].getNext()
    def find(self,content):
        pointer = self.TopPointer
        while pointer != -1:
            if self.Elements[pointer].getContent() == content:
                return pointer
            print(f"pointer={pointer},content={self.Elements[pointer].getContent()}, next = {self.Elements[pointer].getNext()}")
            pointer = self.Elements[pointer].getNext()
        return None


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




if __name__ == "__main__":
    # test
    # I Love Console Interface
    linkedlist = LinkedList_V2(Node("a", -1))
    while True:
        cmd = input("Please Input")
        match cmd:
            case "a":
                a = input("Append What")
                linkedlist.add_element(a)
                print(f"OK, Added")
            case "d":
                d = input("Delete What")
                print("Trying to Remove ELEMENT" + d)
                linkedlist.remove_element(d)
            case "p":
                linkedlist.output()
            case "s":
                s = input("Search What")
                print(linkedlist.find(s))
            case "l":
                with open("person.pickle", "rb") as file:
                    linkedlist = pickle.load(file)
            case "i":
                s = input("INSERT What")
                a = int(input("INSERT WHERE"))
                linkedlist.insert_element(a, s)
        with open("person.pickle", "wb") as f:
            pickle.dump(linkedlist, f)