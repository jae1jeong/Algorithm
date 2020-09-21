

class Node:

    '''Node has data, next(pointer)'''

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        new_node = Node(data)

        if self.head == '':
            self.head = new_node  # 방어 코드
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def print_all(self):
        # print all of the linkedlist
        node = self.head

        while node:
            print(node.data)
            node = node.next

    def delete(self, data):

        if self.head == None:
            return 'No data here'
        cur = self.head

        # head 데이터인 경우 
        if cur.data == data:
            self.head = self.head.next
            del cur

        else:
            cur = self.head
            while cur.next:
                if cur.next.data == data:
                    temp = cur.next
                    cur.next = cur.next.next
                    del temp
                else:
                    cur = cur.next


# main code
if __name__ == '__main__':
    llst = LinkedList(1)
    llst.print_all()
    print('------------------')
    for i in range(2, 10):
        llst.add(i)
    llst.print_all()
    llst.delete(9)
    print('------------------')
    llst.print_all()
    llst.delete(0)
    print('------------------')
    llst.print_all()
    print('------------------')
    llst.delete(5)
    llst.print_all()



