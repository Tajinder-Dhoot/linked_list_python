from linked_list import LinkedList
from linked_list import Node

def merge_sort(linked_list):
    
    if linked_list.size() == 1:
        return linked_list
    
    if linked_list.size() == 0:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def merge(left_linked_list, right_linked_list):
    left_linked_list_size = left_linked_list.size()
    right_linked_list_size = right_linked_list.size()
    merged_linked_list = LinkedList()
    
    left_list_current_node = left_linked_list.head
    right_list_current_node = right_linked_list.head
    left_node_count = 0
    right_node_count = 0
    node_count = 0

    while left_node_count < left_linked_list_size and right_node_count < right_linked_list_size:
        if left_list_current_node.value < right_list_current_node.value:
            merged_linked_list.insert(left_list_current_node.value, node_count)
            left_list_current_node = left_list_current_node.next_node
            left_node_count += 1
        else:
            merged_linked_list.insert(right_list_current_node.value, node_count)
            right_list_current_node = right_list_current_node.next_node
            right_node_count += 1

        node_count += 1

    while left_node_count < left_linked_list_size:
        merged_linked_list.insert(left_list_current_node.value, node_count)
        left_list_current_node = left_list_current_node.next_node
        left_node_count += 1
        node_count += 1

    while right_node_count < right_linked_list_size:
        merged_linked_list.insert(right_list_current_node.value, node_count)
        right_list_current_node = right_list_current_node.next_node
        right_node_count += 1
        node_count += 1

    return merged_linked_list


def split(linked_list):
    left_linked_list = LinkedList()
    right_linked_list = LinkedList()
    # left_linked_list.head = linked_list.head
    current_node = linked_list.head
    node_count = 0
    linked_list_size = linked_list.size()
    mid = linked_list_size // 2

    while node_count < mid:
        left_linked_list.insert(current_node.value, node_count)
        current_node = current_node.next_node
        node_count += 1

    while node_count >= mid  and node_count < linked_list_size:
        right_linked_list.insert(current_node.value, node_count - mid)
        current_node = current_node.next_node
        node_count += 1
        
    return left_linked_list, right_linked_list

l = LinkedList()
l.add(5)
l.add(1)
l.add(7)
l.add(4)
l.add(8)
l.add(2)
l.add(6)
l.add(6)

print(l)
print(merge_sort(l))