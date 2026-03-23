# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 1. Khởi tạo danh sách
nums = list(map(int, input("Nhập danh sách số nguyên (cách nhau bằng dấu cách): ").split()))
print("Danh sách ban đầu:", nums)


# 2. Thêm phần tử
x = int(input("Nhập số cần thêm: "))
nums.append(x)
print("Sau khi thêm:", nums)


# 3. Đếm số lần xuất hiện của k
k = int(input("Nhập giá trị k cần đếm: "))
count = nums.count(k)
print(f"Số lần xuất hiện của {k} là:", count)


# 4. Tính tổng số nguyên tố
tong = 0
for num in nums:
    if la_so_nguyen_to(num):
        tong += num
print("Tổng các số nguyên tố:", tong)


# 5. Sắp xếp danh sách (tăng dần)
nums.sort()
print("Danh sách sau khi sắp xếp:", nums)


# 6. Xóa danh sách
nums.clear()
print("Danh sách sau khi xóa:", nums)