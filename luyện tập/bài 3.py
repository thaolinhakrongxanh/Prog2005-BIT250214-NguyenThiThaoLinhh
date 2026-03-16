# Nhập tên người dùng
name = input("Nhập tên: ")

# Bỏ khoảng trắng ở đầu và cuối
name = name.strip()

# Tách các từ trong chuỗi
words = name.split()

# Chuẩn hóa từng từ
result = ""
for w in words:
    result = result + w.capitalize() + " "

# Bỏ khoảng trắng thừa cuối chuỗi
result = result.strip()

# In kết quả
print("Tên sau khi chuẩn hóa:", result)