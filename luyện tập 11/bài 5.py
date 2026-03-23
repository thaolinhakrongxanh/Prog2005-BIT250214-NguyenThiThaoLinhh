# Tạo dictionary
my_dict = {
    "name": "Linh",
    "age": 18,
    "city": "Ha Noi"
}

# Nhập key cần kiểm tra
key = input("Nhập key cần kiểm tra: ")

# Kiểm tra
if key in my_dict:
    print("✅ Key tồn tại trong dictionary")
else:
    print("❌ Key không tồn tại")