from typing import List


class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def convertArr2LL(arr: List[int]) -> Node:
    head = Node(arr[0])
    mover = head
    for i in arr[1:]:
        temp = Node(i)
        mover.next = temp
        mover = temp
    return head


def lengthLL(head: Node) -> int:
    count = 0
    temp = head
    while temp:
        count = count + 1
        temp = temp.next
    return count


def checkIfPresent(head: Node, search: int) -> int:
    temp = head
    count = 0
    while temp:
        count = count+1
        if search == temp.data:
            return count
        temp = temp.next
    return -1


def removeHead(head) -> Node:
    if head==None: return head
    else:
        temp = head
        head = head.next
        return head

def removeTail(head):
    if head == None or head.next == None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head

if __name__ == "__main__":
    arr = [1, 4, 6, 9]
    head = convertArr2LL(arr=arr)
    newHead = removeTail(head=head)
    temp = newHead  # we don't want to tamper the head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("null\n")
