# Nhập chuỗi
s = input("Nhập chuỗi: ")

hoa = 0
thuong = 0
so = 0
dacbiet = 0
khoangtrang = 0
nguyenam = 0
phuam = 0

for c in s:
    if c.isupper():
        hoa += 1
    if c.islower():
        thuong += 1
    if c.isdigit():
        so += 1
    if c.isspace():
        khoangtrang += 1

    # kiểm tra nguyên âm
    if c.lower() in "aeiou":
        nguyenam += 1

    # kiểm tra phụ âm
    elif c.isalpha():
        phuam += 1

    # ký tự đặc biệt
    if not c.isalnum() and not c.isspace():
        dacbiet += 1

print("Số chữ in hoa:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ số:", so)
print("Số ký tự đặc biệt:", dacbiet)
print("Số khoảng trắng:", khoangtrang)
print("Số nguyên âm:", nguyenam)
print("Số phụ âm:", phuam)