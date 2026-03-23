import csv

# 1. Nhập thông tin
name = input("Nhập tên nhân viên: ")
age = input("Nhập tuổi: ")
emp_id = input("Nhập ID: ")

# 2. Lưu vào file TXT
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {name}\n")
    f.write(f"Tuổi: {age}\n")
    f.write(f"ID: {emp_id}\n")

print("✅ Đã lưu file nhanvien.txt")


# 3. Lưu vào file CSV
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])   # tiêu đề
    writer.writerow([name, age, emp_id])     # dữ liệu

print("✅ Đã lưu file nhanvien.csv")


# 4. Hiển thị nội dung file (giống như "chụp ảnh")
print("\n📄 Nội dung file TXT:")
with open("nhanvien.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("\n📄 Nội dung file CSV:")
with open("nhanvien.csv", "r", encoding="utf-8") as f:
    print(f.read())