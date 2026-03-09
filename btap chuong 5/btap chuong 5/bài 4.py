n = int(input("Nhập số phần tử"))

a = []
for i in range(n):
    a.append(int(input("Nhập phần tử"))

for i in range(n - 1):
    max_index = i
    for j in range(i + 1, n):
        if a[j] > a[max_index]:
            max_index = j

    a[i], a[max_index] = a[max_index], a[i]

    for x in a:
        print(x, end=" ")
    print()