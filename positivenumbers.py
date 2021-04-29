list1 = [12, -7, 5, 64, -14]
for number in list1:
    if number >=0:
        print(number, end =",")

list2 =[12, 14, -95, 3]
num = list(filter(lambda x : x >0, list2))
print(num)
