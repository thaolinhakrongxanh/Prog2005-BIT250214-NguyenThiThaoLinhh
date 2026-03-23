# Nhập số lượng người
n = int(input("Nhập số người: "))

# 1 + 2. Nhập và lưu vào dict
data = {}

for i in range(n):
    name = input(f"Nhập tên người {i + 1}: ")
    age = int(input(f"Nhập tuổi của {name}: "))
    data[name] = age

print("\nDictionary ban đầu:", data)

# 3. Tính tuổi trung bình
tong = sum(data.values())
avg = tong / n
print("Tuổi trung bình:", avg)

# 4. Selection sort theo tuổi giảm dần
items = list(data.items())  # chuyển sang list để sắp xếp

for i in range(len(items)):
    max_idx = i
    for j in range(i + 1, len(items)):
        if items[j][1] > items[max_idx][1]:  # so sánh tuổi
            max_idx = j

    # đổi chỗ
    items[i], items[max_idx] = items[max_idx], items[i]

# In kết quả
print("\nDanh sách sau khi sắp xếp (giảm dần theo tuổi):")
for name, age in items:
    print(name, ":", age)