# Nhập số từ bàn phím
n = int(input("Nhập một số: "))

tong = 0

while n > 0:
    chu_so = n % 10      # Lấy chữ số cuối
    tong = tong + chu_so # Cộng vào tổng
    n = n // 10          # Bỏ chữ số cuối

print("Tổng các chữ số là:", tong)