total = 0
maxMarks = 5

for i in range(maxMarks):
    print("Mark #", i+1, " = ", end = "")
    mark = int(input())
    total = total + mark
print(total/maxMarks)
