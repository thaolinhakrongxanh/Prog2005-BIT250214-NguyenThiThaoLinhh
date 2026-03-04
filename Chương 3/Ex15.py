#Dùng Slicing
s = input("Nhập chuỗi: ")
print("Chuỗi đảo ngược:", s[::-1])


#Không dùng Slicing
s = input()
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

print("Chuỗi đảo ngược:", reversed_s)