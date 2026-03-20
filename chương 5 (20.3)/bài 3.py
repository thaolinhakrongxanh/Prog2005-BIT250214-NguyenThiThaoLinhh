# Import thư viện
import matplotlib.pyplot as plt

# Dữ liệu
san_pham = ["A", "B", "C", "D", "E"]
phan_tram = [30, 25, 15, 20, 10]

# Vẽ biểu đồ tròn
plt.pie(phan_tram, labels=san_pham, autopct='%1.1f%%')

# Tiêu đề
plt.title("Tỷ lệ doanh số của các sản phẩm")

# Hiển thị
plt.show()