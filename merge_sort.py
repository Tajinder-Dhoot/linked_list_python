def merge_sort(list):
    """
    sorts a list in ascending order
    returns a new sorted list

    Divide : Find the midpoint of the list and divide into sublists
    Conquer: recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in previous steps
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    # print(split(list))

    print("left half: ",left_half)
    print("right half: ",right_half)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # return left, right
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at themidpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) runtime
    """

    mid = len(list)//2
    left_half = list[:mid]
    right_half = list[mid: ]
    
    return left_half, right_half

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    """

    l= []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i +=1
        else:
            l.append(right[j])
            j +=1

    while i < len(left):
        l.append(left[i])
        i +=1

    while j < len(right):
        l.append(right[j])
        j +=1

    return l

def factorial(n):

    if n < 1:
        return 0
    if n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(6))

l = [1,8,6,3,4,9,7]
# print(split(l))
print( merge_sort(l))