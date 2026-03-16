class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    # Nạp chồng toán tử ==
    def __eq__(self, other):
        return self.diem == other.diem


# Tạo các đối tượng sinh viên
sv1 = SinhVien(8)
sv2 = SinhVien(8)
sv3 = SinhVien(7)

# So sánh
print(sv1 == sv2)  # True vì điểm bằng nhau
print(sv1 == sv3)  # False vì điểm khác nhau