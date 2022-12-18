import sys
import time
from load import load_numbers

start_time = time.time()
print(sys.getrecursionlimit())
sys.setrecursionlimit(20001)
print(sys.getrecursionlimit())

def selectionSort(values):

    if(len(values) == 1):
        return values

    sorted_values = []
    min_value_index = getMinValueIndex(values)
    sorted_values.append(values.pop(min_value_index))
    
    return sorted_values + selectionSort(values)

def getMinValueIndex(values):
    min_value = values[0]
    min_value_index = 0

    for i in range(1,len(values)):
        if values[i] < min_value:
            min_value = values[i]
            min_value_index = i

    return min_value_index

# numbers = [1,-6,82,2,3,8,6,4,15,12]
# numbers = [5,3,8,10,1]
numbers = load_numbers(sys.argv[1])
print(selectionSort(numbers))
end_time = time.time()
execution_time = end_time - start_time
print("execution time for selection sort: ", execution_time)