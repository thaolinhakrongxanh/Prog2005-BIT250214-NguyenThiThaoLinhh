arr = list(map(int, input().split()))

found = False
for num in arr:
    if num > 10:
        print("Số đầu tiên lớn hơn 10:", num)
        found = True
        break

if not found:
    print("Không có số nào lớn hơn 10")