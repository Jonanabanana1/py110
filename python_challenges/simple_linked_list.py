"""
Goal: Write simple linked list implementation
Create 2 Classes, an Element class and a SimpleLinkedList Class

Element:
    - Constructor requires an integer representing datum, and an optional second element representing the previous element in the stack
    - If an element doesn't have a previous element, it is considered a tail
    - Should have an is_tail() method that returns a boolean.
    - If element doesn't have a previous element, element.next returns None
    - element.next should return the previous element

SimpleLinkedList:
    X Constructor has no parameters
    X Has a .size property
    X Has an is_empty() method
    X Has a method push(object) that pushes an object into the linked list
        Whenever an object is pushed, the linked list should push an element in place of the object.
        The element's datum should reference the object
    X Has a lst.head property that should reference the latest element in the stacked list
    X Has a peek() method that returns the top element's datum, if the list is empty should return None
    X Has a pop() method that removes and returns the top element from the list
    X Has a method from_list() that accepts a list as an argument and converts the list to a linked list
        Elements in the list are added from right to left to the linked list
        Elements at the end of the list argument are added first, and the first element in the list is added last to the linked list
        If None is passed as the argument, create an empty linked list
    X Has a method to_list() that converts the linked list to a regular list
        first element in regular list should be the top element of linked list.
        Append to the regular list by just popping out elements from the linked list
    - Has a method to reverse() that reversed the order of the linked list
        - Create a new linked list, add elemeents from the old linked list to the new linked list and the new one should be the old one reversed

"""


class Element:
    def __init__(self, datum, next_element=None) -> None:
        if not isinstance(next_element, Element):
            next_element = None
        self._datum = datum
        self._next = next_element

    @property
    def datum(self) -> any:
        return self._datum

    @property
    def next(self) -> "Element":
        return self._next

    def is_tail(self) -> bool:
        return self.next is None


class SimpleLinkedList:
    def __init__(self) -> None:
        self._size = 0
        self._head = None

    @property
    def size(self) -> int:
        return self._size

    @property
    def head(self) -> Element:
        return self._head

    def is_empty(self) -> bool:
        return self.size == 0

    def peek(self) -> any:
        if self.head is None:
            return None
        return self.head.datum

    def push(self, obj) -> None:
        new_element = Element(obj, self.head)
        self._head = new_element
        self._size += 1

    def pop(self) -> any:
        if self.is_empty():
            return None
        old_head = self.head
        new_head = self.head.next
        self._head = new_head
        self._size -= 1
        return old_head.datum

    @classmethod
    def from_list(cls, lst: list | None) -> "SimpleLinkedList":
        new_linked_list = SimpleLinkedList()
        if lst is None:
            return new_linked_list

        start_idx_inclusive = len(lst) - 1
        end_idx_exclusive = -1
        step = -1

        for idx in range(start_idx_inclusive, end_idx_exclusive, step):
            new_linked_list.push(lst[idx])

        return new_linked_list

    def to_list(self) -> list:
        new_list = []
        current_head = self.head

        for _ in range(self.size):
            new_list.append(current_head.datum)
            current_head = current_head.next
        return new_list

    def reverse(self) -> "SimpleLinkedList":
        rev_linked_list = SimpleLinkedList()
        current_head = self.head

        for _ in range(self.size):
            rev_linked_list.push(current_head.datum)
            current_head = current_head.next

        return rev_linked_list
