n = int(input("Nhập n: "))

# Hình 1: hình vuông
print("\nHình 1:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Hình 2: tam giác vuông trái
print("\nHình 2:")
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Hình 3: tam giác vuông ngược
print("\nHình 3:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Hình 4: tam giác cân
print("\nHình 4:")
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()

# Hình 5: tam giác lệch trái
print("\nHình 5:")
for i in range(1, n+1):
    print(" " * (i-1), end="")
    for j in range(i):
        print("*", end=" ")
    print()

# Hình 6: chữ L
print("\nHình 6:")
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 7: tam giác phải
print("\nHình 7:")
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

# Hình 8: hình thoi
print("\nHình 8:")
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()

# Hình 9: chữ V
print("\nHình 9:")
for i in range(n):
    for j in range(2*n):
        if j == i or j == 2*n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Hình 10: chữ X
print("\nHình 10:")
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()