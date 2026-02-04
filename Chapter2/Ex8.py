n = int(input("Nhập số: "))
dao = 0

while n > 0:
    dao = dao*10 + n % 10
    n //= 10

print(dao)
