# In các số lẻ từ 111 đến 17 (giảm dần)
print("Các số lẻ từ 111 đến 17:")
for i in range(111, 16, -1):
    if i % 2 != 0:
        print(i, end=" ")

print("\n")

# In các số nguyên tố từ 111 đến 17 (giảm dần)
print("Các số nguyên tố từ 111 đến 17:")

for i in range(111, 16, -1):
    is_prime = True

    if i < 2:
        is_prime = False
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

    if is_prime:
        print(i, end=" ")
