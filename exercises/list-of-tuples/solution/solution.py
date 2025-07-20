len = int(input())
listge = []
while len > 0:
    len -= 2
    name = input()
    student_number = int(input())
    listge.append((name, student_number))

print(listge)