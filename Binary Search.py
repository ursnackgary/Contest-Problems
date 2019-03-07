# With comments
import random
'''
variables:
length: the length of the number list
point: the value you are searching for
numbers: the list of randomly generated number
'''

length = int(input('Length of the list: '))
point = int(input('Enter a number: '))
numbers = [random.randint(1, 10) for n in range(length)]
numbers.sort()

'''
head: the index offirst number of the selected list
tail:  the index of last number of the selected list
middle: the index middle number of the selected list
'''
head = 0
middle = length // 2
tail = length - 1

#Loop through the list
while True:
    # if the index of the middle number euqals to the head or the tail of the list, the number is not in the list
    if middle == head or middle == tail:
        print("Number is not in the list")
        break

    # if the first number equals to the number we are searching for, print the index of the head

    if numbers[head] == point:
        print(head)
        break
    # if the last number equals to the number we are searching for, print the index of the head
    elif numbers[tail] == point:
        print(tail)
        break

    # if the middle number equals to the number we are searching for, print the index of the head
    elif numbers[middle] == point:
        print(middle)
        break

    # if the middle number of the current selected list is greater than the value we are searching for, the middle number will become the end of the new selected list
    
    if numbers[middle] > point:
        tail = middle
        middle = int(tail / 2)
        print('big')
       
    # if the middle number of the current selected list is less than the value we are searching for, the middle number will become the start of the new selected list
    if numbers[middle] < point:  
        start = middle
        middle = int(start + ((tail - middle) / 2))
        print('small')

# print the list       
print(numbers)
