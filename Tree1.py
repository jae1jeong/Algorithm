# 트리 구조
'''
트리: Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
실제로 어디에 많이 사용되나?
    트리 중 이진 트리(Binary Tree)형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

Parent Node: 어떤 노드의 다음 레벨에 연결된 노드
Child Node: 어떤 노드의 상위 레벨에 연결된 노드
Leaf Node(Terminal Node): Child Node가 하나도 없는 노드
Sibling(Brother Node):동일한 Parent Node를 가진 노드
Depth:트리에서 Node가 가질 수 있는 최대 Level
'''

'''
이진 트리와 이진 탐색 트리(Binary Search Tree)는 서로 다름
이진 트리: 노드의 최대 Branch가 2인 트리
이진 탐색 트리(Binary Search Tree,BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
    왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음


이진 탐색 트리의 장점과 주요 용도
주요 용도 데이터 검색(탐색)
장점: 탐색 속도를 개선 할 수 있음
단점: 이진 탐색 트리 알고리즘 이해 후
'''
# 이진 탐색 트리 만들기


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


head = Node(1)  # 새 노드 생성
BST = NodeMgmt(head)  # 이진탐색트리에 head에 삽입함으로써 루트 노드가 됨
BST.insert(2)
BST.insert(3)
BST.insert(6)
BST.insert(1)
BST.insert(5)
BST.insert(8)

print(BST.search(-1))  # False
print(BST.search(8))  # True
