

class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:

    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    # 맨 뒤에 Node를 추가한다.
    def add(self, data):

        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head

        else:

            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            self.tail = new_node

    # 링크드 리스트 전체를 출력한다.
    def desc(self):
        cur = self.head
        if cur == None:
            return 'No data here'

        while cur:
            print(cur.data)
            cur = cur.next

    # 링크드 리스트 앞에서부터 찾는다.
    def search_from_head(self, data):

        if self.head == None:
            return 'No data here'

        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                print(node.data)
                node = node.next
        return False

    # 링크드 리스트 뒤에서부터 찾는다.
    def search_from_tail(self, data):

        if self.head == None:
            return 'No data here'

        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                print(node.data)
                node = node.prev

        return False

    # 인자 데이터를 찾아
    def insert_before(self, data, before_data):

        if self.head == None:
            self.head = Node(data)

        else:
            cur = self.tail
            while cur.data != before_data:
                cur = cur.prev
                if cur == None:
                    return False
            new = Node(data)
            before = cur.prev
            before.next = new
            new.prev = before
            new.next = cur
            cur.prev = new
            return True


# test code
if __name__ == '__main__':
    dll = DoubleLinkedList(5)

    for i in range(10):
        dll.add(i)
    # dll.desc()
    node5 = dll.search_from_head(6)
    if node5:
        print(f'node5 is {node5.data}')
    else:
        print('no data here')
    node7 = dll.search_from_tail(7)
    if node7:
        print(f'node7 is {node7.data}')
    else:
        print('no data here')

    dll.insert_before(5.5, 6)
    dll.desc()
