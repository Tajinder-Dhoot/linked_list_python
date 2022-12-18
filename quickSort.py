def quickSort(list):

    if(len(list) <= 1):
        return list
    
    pivot = list[0]
    remaining_list = list[1:]
    less_than_pivot, higher_than_pivot = split(remaining_list, pivot)
    lowest = quickSort(less_than_pivot)
    highest = quickSort(higher_than_pivot)

    return quickSort(less_than_pivot) + [pivot] + quickSort(higher_than_pivot)

def split(list, target):
    lower_values = []
    higher_values = []
    for number in list:
        if number <= target:
            lower_values.append(number)
        else:
            higher_values.append(number)

    return lower_values, higher_values

numbers = [1,-6,82,2,3,8,6,4,15,12]
# numbers = [5,3,8,10,1]

print(quickSort(numbers))