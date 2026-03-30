import math

# Nhập số
num = float(input("Nhập một số: "))

# Kiểm tra
if num < 0:
    print("Lỗi: Không thể tính căn bậc hai của số âm!")
else:
    result = math.sqrt(num)
    print("Căn bậc hai của", num, "là:", result)

