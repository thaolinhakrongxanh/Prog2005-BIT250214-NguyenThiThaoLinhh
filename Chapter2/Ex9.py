n = int(input("Nhập số: "))
max_digit = 0

while n > 0:
    d = n % 10
    if d > max_digit:
        max_digit = d
    n //= 10

print(max_digit)
