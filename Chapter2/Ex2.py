n = int(input("Nhập số dương: "))

if n < 2:
    print("Không phải số nguyên tố")
else:
    la_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to:
        print("Là số nguyên tố")
    else:
        print("Không phải số nguyên tố")
