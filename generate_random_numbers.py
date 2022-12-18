import random
from write_data_to_file import writeDataToFile

def generateRandomNumbersBetween(lower_limit, upper_limit):
    numbers = []
    for i in range(lower_limit, upper_limit):
        numbers.append(random.randrange(lower_limit,upper_limit))
    
    return numbers

numbers = generateRandomNumbersBetween(0,10000)
print(numbers)

# writeDataToFile(numbers, './numbers/10_numbers.txt')
# writeDataToFile(numbers, './numbers/100_numbers.txt')
# writeDataToFile(numbers, './numbers/1000_numbers.txt')
writeDataToFile(numbers, './numbers/10000_numbers.txt')
# writeDataToFile(numbers, './numbers/1_million_numbers.txt')