import ll


class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Empty LL")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def get_len(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at(self,index,data):
        if index<0 or index> self.get_len():
            raise Exception("Index out of range")
            return

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0

        while itr:
            if index == count - 1:
                node = Node(data,itr.next)
                itr.next = node
            itr = itr.next
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def remove_at(self,index):
        if index < 0 or index > self.get_len():
            raise Exception("Invalid")
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
            itr = itr.next

    def remove_by_value(self,data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()