# Pseudocode and Python worksheet

#1
total:int = 0
average:float = 0
number_of_marks:int = 5
for counter in range(number_of_marks):
    mark:int = int(input("Enter mark: "))
    total = total + mark
#next counter
average = total / number_of_marks
print(f"Total = {total}\tAverage = {average}\n")

#2
valid_inputs:int = 0
while True:
    number:int = int(input("Enter a positive integer: "))
    if number == -1:
        break
    elif number <= 0:
        print("Invalid input, must be positive or -1 to stop")
    else:
        valid_inputs = valid_inputs + 1
    #endif
#endwhile
print("Valid inputs =", valid_inputs)

#3
how_many_students:int = int(input("How many students? "))
score:int = int(input("Score: "))
highest:int = score
lowest:int  = score
for counter in range(how_many_students-1):
    score = int(input("Score: "))
    if score > highest:
        highest = score
    #endif
    if score < lowest:
        lowest = score
#next counter
print("Highest score =", highest, "Lowest score =", lowest)
#3 with 1D array
how_many_students:int = int(input("How many students? "))
scores = [0] * how_many_students #DECLARE Scores[0..how_many_students] OF INTEGER
for counter in range(how_many_students):
    scores[counter] = int(input("Score: "))
    print(f"Scores #{counter} = {scores[counter]}")
#next counter
highest:int = scores[0]
lowest:int = scores[0]
for index in range(1, len(scores)):
    if scores[index] > highest:
        highest = score
    #endif
#next index
print("Highest score =", highest)

#4
scores:list = [45, 62, 78, 55, 90, 68]
total:int = 0

for index in range(len(scores)):
    print(scores[index])
    total = total + scores[index]
#next index
print("Average =", total/len(scores))

#5
temperatures:list = [28, 31, 29, 32, 30, 33, 27]
high:int = 30
count_highs:int = 0
for index in range(len(temperatures)):
    if temperatures[index] > high:
        count_highs = count_highs + 1
print("Days above", high, " degrees = ", count_highs)

#6
names:list = ["Ali","Sarah","Dev","Mei","Carlos"]
search:str = input("Enter name to find: ").strip()
found:bool = False
print(names)
for index in range(len(names)):
    if search.lower() == names[index].lower():
        found = True
        print(f"{search} found at position/index {index}.")
if found == False:
    print(f"{search} not found.")
