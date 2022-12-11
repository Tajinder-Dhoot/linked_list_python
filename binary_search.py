def BinarySearch(list, target):
    """
        list should be sorted
        comapre the target element with mid element, if equals true/ false or index of target element found
        if not found at mid, check if target is smaller  or greateer thean the mid
        if smaller, take first half and find the mid of it and repeat above 2 steps
        if greater, take second half and find the mid of it and repeat above 2 steps
    """
    mid = len(list)//2
    if list[mid]  == target:
        return True

    if len(list) == 1 and list[mid]  != target:
        return False

    if target < list[mid]:
            return BinarySearch(list[:mid], target)
    else:
        return BinarySearch(list[mid + 1:], target)   

list = [1,2,3,9,12,45,56,87,101]
target = 5

print(BinarySearch(list, target))
