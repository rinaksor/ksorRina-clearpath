a = [7, 2, 4, 6]
max_number = a[0] 

for i in range(1, len(a)):
    if a[i] > max_number:
        max_number = a[i]

print("Số lớn nhất trong mảng là:", max_number)