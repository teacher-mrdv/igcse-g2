## The code commented below (lines 3~10) creates an array of 10
## random integers (array_length) within the range defined by the lowest~highest pair of variables
#import random
#lowest = 1
#highest = 100
#array = []
#array_length = 10
#for counter in range(array_length):
#    array.append(random.randint(lowest, highest))
#print(array)

# We use the array below to get consistent results
array = [71, 63, 70, 20, 7, 54, 85, 90, 76, 99, 60, 38, 44, 96, 17, 15, 61, 48, 19, 84, 97, 22, 50, 25, 36, 39, 79, 88, 71, 52, 4, 15, 11, 78, 54, 31, 12, 27, 62, 60, 3, 54, 27, 86, 94, 76, 62, 47, 38, 96, 15, 93, 45, 93, 96, 85, 11, 84, 72, 11, 74, 64, 57, 35, 70, 67, 86, 30, 1, 42, 28, 7, 18, 44, 92, 58, 32, 39, 75, 90, 7, 65, 23, 93, 12, 93, 86, 16, 97, 21, 63, 41, 24, 64, 26, 94, 25, 87, 55, 27]
array_length = len(array)
#print("array =", array, "\n array length =", array_length)

# printing the array (with indices)
for index in range(array_length):
    print("index =" , index, ": value =", array[index])
print() # leave empty line (same as \n)

# min & max
minimum = array[0]
maximum = array[0]
# we start at index 1 because index 0 is the initial min and max values
for index in range(1, array_length):
    if array[index] < minimum:
        minimum = array[index]
    if array[index] > maximum:
        maximum = array[index]
print("Minimum = ", minimum)
print("Maximum = ", maximum)

# totalling
total = 0
for index in range(array_length):
    total = total + array[index]
print("Total   =", total)
average = total / len(array)
print("Average =", average)

# counting only (above average)
above_average = 0
for index in range(array_length):
    if array[index] > average:
        above_average = above_average + 1
print("Values above average =", above_average)

# linear search and counting
print("\nInput a number to search for: ", end="")
key = int(input())
frequency = 0
for index in range(array_length):
    if array[index] == key:
        frequency = frequency + 1
        print(key, "found at index", index)
if frequency == 0:
    print(key, "not found")
else:
    print(key, "found", frequency,"times.")
print()

# bubble sort
lastIndex = len(array)-1
swapped = True
while lastIndex > 0 and swapped:
    swapped = False 
    for index in range(lastIndex):
        if array[index] > array[index+1]:
            temp = array[index]
            array[index] = array[index+1]
            array[index+1] = temp
            swapped = True
        #endif
    #next index
    lastIndex = lastIndex - 1
#endwhile
print(array)
print("\nWith the array sorted, the minimum and maximum are as easy as\noutputting array[0] and array[len(array)-1] to get\nthe first and last items in the array.")
print("\narray[0] =", array[0], "    array[len(array)-1] =", array[len(array)-1])
