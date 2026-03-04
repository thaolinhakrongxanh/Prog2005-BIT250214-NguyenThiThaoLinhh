arr = list(map(int, input().split()))

even_sum = 0
print("Các số chẵn:")
for num in arr:
    if num % 2 == 0:
        print(num)
        even_sum += num

print("Tổng các số chẵn:", even_sum)