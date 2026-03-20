# Bước 1: import thư viện
import matplotlib.pyplot as plt

# Bước 2: dữ liệu
xep_loai = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
so_luong = [6, 10, 12, 4, 1]

# Bước 3: vẽ biểu đồ cột
plt.bar(xep_loai, so_luong)

# Bước 4: thêm tiêu đề và nhãn
plt.title("Biểu đồ kết quả học tập của lớp")
plt.xlabel("Xếp loại")
plt.ylabel("Số lượng học sinh")

# Bước 5: hiển thị số trên đầu mỗi cột (cho đẹp)
for i in range(len(so_luong)):
    plt.text(i, so_luong[i], str(so_luong[i]), ha='center')

# Bước 6: hiển thị lưới (tùy chọn)
plt.grid()

# Bước 7: hiển thị biểu đồ
plt.show()