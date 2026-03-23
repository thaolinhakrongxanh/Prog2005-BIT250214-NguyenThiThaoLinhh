# Nhập danh sách số
nums = input("Nhập các số cách nhau bằng dấu cách: ").split()

# Chuyển sang số nguyên
nums = [int(x) for x in nums]

even_numbers = []
total = 0

# Duyệt danh sách
for num in nums:
    if num % 2 == 0:
        even_numbers.append(num)
        total += num

# In kết quả
print("Các số chẵn:", even_numbers)
print("Tổng các số chẵn:", total)