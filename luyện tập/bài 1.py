# Nhập cân nặng
weight = float(input("Nhập cân nặng (kg): "))

# Nhập chiều cao
height = float(input("Nhập chiều cao (m): "))

# Tính BMI
bmi = weight / (height * height)

# In kết quả (làm tròn 2 chữ số)
print("BMI của bạn là:", round(bmi, 2))