

# 힙은 데이터에서 최대값이나 최소값을 빠르게 찾귀 위해 고안된 완전 이진 트리
'''
완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리
'''


class Heap:

    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def __str__(self):
        return f'{self.heap_array[1:]}'

    def Insertheap(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)  # Just in case
            return True

        self.heap_array.append(data)

        inserted_idx = len(self.heap_array)-1  # None이 있기 때문에

        while self.move_up(inserted_idx):  # return 값이 True 일때까지만
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx]
            # Swap
            self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx], self.heap_array[parent_idx]
            inserted_idx = parent_idx  # 부모 노드가 되어서 상단 노드와 비교

        return True

    def move_up(self, inserted_idx: int):
        if inserted_idx <= 1:  # 제일 위에 갔을때(다 올라간 상태)
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:  # 부모 노드가 더 크다면 False 리턴
            return False

    def move_down(self, popped_index: int):
        left_child_popped_index = popped_index * 2
        right_child_popped_index = popped_index * 2 + 1

        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_index >= len(self.heap_array):
            return False

        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_index >= len(self.heap_array):
            if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:  # 자식이 더 클때
                return True
            else:
                return False

        # case3: 둘 다 있을때
        else:
            if self.heap_array[left_child_popped_index] > self.heap_array[right_child_popped_index]:
                if self.heap_array[popped_index] > self.heap_array[left_child_popped_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_popped_index] > self.heap_array[popped_index]:
                    return True
                else:
                    return False

    def pop_heap(self):
        if len(self.heap_array) <= 1:
            return None  # False보다는 노드의 값을 리턴해야되기 때문에 None이 적합

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_index = 1
        while self.move_down(popped_index):
            left_child_popped_index = popped_index * 2
            right_child_popped_index = popped_index * 2 + 1

            # case2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_index >= len(self.heap_array):
                # 자식이 더 클떄
                if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                    self.heap_array[popped_index], self.heap_array[left_child_popped_index] = self.heap_array[
                        left_child_popped_index], self.heap_array[popped_index]
                    popped_index = left_child_popped_index
            # case3: 둘 다 있을때
            else:
                if self.heap_array[left_child_popped_index] > self.heap_array[right_child_popped_index]:
                    if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                        self.heap_array[popped_index], self.heap_array[left_child_popped_index] = self.heap_array[
                            left_child_popped_index], self.heap_array[popped_index]
                        popped_index = left_child_popped_index
                else:
                    if self.heap_array[right_child_popped_index] > self.heap_array[popped_index]:
                        self.heap_array[popped_index], self.heap_array[right_child_popped_index] = self.heap_array[
                            right_child_popped_index], self.heap_array[popped_index]
                        popped_index = right_child_popped_index

        return returned_data


heap = Heap(15)
heap.Insertheap(10)
heap.Insertheap(8)
heap.Insertheap(5)
heap.Insertheap(4)
heap.Insertheap(20)
print(heap.pop_heap())
print(heap)
heap.Insertheap(23)
print(heap)
heap.Insertheap(25)
print(heap)
