# child node

'''

   이진 탐색 트리 삭제
   경우를 나누어서 생각을 하는게 이해하는데 쉽다.

   Leaf Node삭제
   Leaf Node: Child Node가 없는 Node
   삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.

   Child Node가 하나인 Node  삭제
   삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.

   Child Node가 두 개인 Node 삭제
   1. 삭제할 노드의 오른쪽 자식 중, 가장 작은 값을 찾아서 노드의 Parent 노드가 가리키도록 한다.
   2. 삭제할 노드의 왼쪽 자식 중, 가장 큰 값을 삭제할 노드의 Parent 노드가 가리키도록 한다.


   -삭제할 Node의 오른쪽 자식 선택
   -오른쪽 자식의 가장 왼쪽에 있는 노드를 선택
   해당 노드를 삭제할 노드의 Parent 노드의 왼쪽 Branch가 가리키게 함
   해당 노드의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
   해당 노드의 오른쪽 Branch가 삭제할 노드의 오른쪽 Child Node를 가리키게 함
   만약 해당 노드가 오른쪽 Child 노드를 가지고 있었을 경우에는, 해당 노드의 본래 Parent Node의 왼쪽 Branch가 해당 오른쪽 Child 노드를 가리키게 함.

   사실상 면접에서 말로 설명하기도, 이해하기도 힘듬. 하지만 구현할 수 있어야 함.

    '''


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    '''
    노드를 관리할 수 있는 클래스를 만듬
    '''

    def __init__(self, head):
        self.head = head  # root노드를 head 노드라 지칭

    def insert(self, value):
        self.cur_node = self.head
        while True:
            if value < self.cur_node.value:  # 현재의 노드보다 작기 때문에 왼쪽 노드로 간다.
                if self.cur_node.left != None:  # 브랜치를 가지고 있다면
                    self.cur_node = self.cur_node.left  # 왼쪽 노드로 바꾸고 반복문을 끝낸다.
                else:
                    self.cur_node.left = Node(value)  # 없다면 새로운 노드 삽입
                    break
            else:
                if self.cur_node.right != None:  # if문의 반대니까 value가 크거나 같다 같은 크기의 데이터도 오른쪽으로 간다.
                    self.cur_node = self.cur_node.right
                else:
                    self.cur_node.right = Node(value)
                    break

    def search(self, value):
        self.cur_node = self.head
        while self.cur_node:
            if self.cur_node.value == value:
                return True
            elif self.cur_node.value > value:
                self.cur_node = self.cur_node.left
            else:
                self.cur_node = self.cur_node.right
        # while 문이 다 돌아졌다면 탐색 트리에는 해당 데이터가 없다는 뜻
        return False

    def delete(self, value):
        #  삭제할 노드가 없는 경우도 처리 이를 위해 삭제할 노드가 없는 경우는 False를 리턴하고 함수를 종료 시킨다

        searched = False
        self.cur_node = self.head
        self.parent = self.head

        while self.cur_node:
            if self.cur_node.value == value:
                searched = True
                break
            elif self.cur_node.value > value:
                self.parent = self.cur_node  # parent 노드를 잘 설정하는게 중요
                self.cur_node = self.cur_node.left
            else:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.right

        if searched == False:
            return False

        # 이후부터 Case들을 분리해서 코드 작성
        # cur.node child가 없을 경우
        if self.cur_node.left == None and self.cur_node.right == None:
            if value < self.parent.caule:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.cur_node

        # 삭제할 노드가 Child 노드를 한 개 가지고 있을 경우
        if self.cur_node.left != None and self.cur_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.cur_node.left
            else:
                self.parent.right = self.cur_node.left
        elif self.cur_node.left == None and self.cur_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.cur_node.right
            else:
                self.parent.right = self.cur_node.right

        # 삭제할 노드가 Child 노드를 두 개 가지고 있을 경우(삭제할 Parent 노드 왼쪽에 있을 때)

        # 삭제할 노드의 오른쪽 자식 중, 가장 작은 값을 노드의 Parent 노드가 가리키도록 한다
        또 다시 삭제할 노드가
