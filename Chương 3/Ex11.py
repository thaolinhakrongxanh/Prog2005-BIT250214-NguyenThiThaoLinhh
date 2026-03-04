arr = list(map(int, input().split()))

max_value = arr[0]
min_value = arr[0]

for num in arr:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Giá trị lớn nhất:", max_value)
print("Giá trị nhỏ nhất:", min_value)