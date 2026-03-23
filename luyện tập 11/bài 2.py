# Nhập 5 chuỗi
arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    arr.append(s)

# Sắp xếp trước (theo ABC)
arr.sort()

print("\nDanh sách sau khi sắp xếp:", arr)

# Nhập chuỗi cần tìm
x = input("\nNhập chuỗi cần tìm: ")

# Binary Search
left = 0
right = len(arr) - 1
found = False

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == x:
        print(f"✅ Tìm thấy tại vị trí: {mid}")
        found = True
        break
    elif x < arr[mid]:
        right = mid - 1
    else:
        left = mid + 1

if not found:
    print("❌ Không tìm thấy chuỗi trong danh sách")