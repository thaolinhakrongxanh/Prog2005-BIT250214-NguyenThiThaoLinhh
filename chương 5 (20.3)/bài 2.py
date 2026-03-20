# Import thư viện
import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu
x = np.linspace(-5, 5, 100)

# Định nghĩa hàm số
y1 = x**2   # y = x^2
y2 = x**3   # y = x^3

# Vẽ đồ thị
plt.plot(x, y1, color="blue", label="y = x^2")
plt.plot(x, y2, color="red", label="y = x^3")

# Thêm tiêu đề và nhãn trục
plt.title("Đồ thị của y = x^2 và y = x^3")
plt.xlabel("Giá trị x")
plt.ylabel("Giá trị y")

# Hiển thị chú thích
plt.legend()

# Hiển thị lưới
plt.grid()

# Hiển thị biểu đồ
plt.show()