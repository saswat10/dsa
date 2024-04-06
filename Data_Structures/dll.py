class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def print_list(self):
    current = self.head
    while current:
      print(current.data, end=' <-> ')
      current = current.next

    print("None")

  def array_to_dll(self, data_array):
    self.head = Node(data_array[0])
    prev: Node = self.head
    for element in data_array[1:]:
      temp: Node = Node(element)
      self.prev = self.