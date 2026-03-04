arr = list(map(int, input().split()))
swap_count = 0

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap_count += 1

print("Danh sách sau khi sắp xếp:", arr)
print("Số lần hoán đổi:", swap_count)