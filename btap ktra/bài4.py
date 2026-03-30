def giai_thua(n):
    if n == 0 or n == 1:   # điều kiện dừng
        return 1
    else:
        return n * giai_thua(n - 1)

# Nhập số từ người dùng
n = int(input("Nhập số n: "))

if n < 0:
    print("Không tính được giai thừa của số âm")
else:
    print("Giai thừa của", n, "là:", giai_thua(n))