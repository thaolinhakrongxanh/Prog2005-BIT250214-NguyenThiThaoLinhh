class SinhVien:
    so_luong = 0   # biến của class để đếm số sinh viên

    def __init__(self, ten):
        self.ten = ten
        SinhVien.so_luong += 1   # mỗi lần tạo đối tượng thì tăng lên 1

    @classmethod
    def dem_sinh_vien(cls):
        print("Số sinh viên đã tạo:", cls.so_luong)


# Tạo các đối tượng sinh viên
sv1 = SinhVien("Long")
sv2 = SinhVien("Linh")
sv3 = SinhVien("Trúc")

# Gọi class method để đếm
SinhVien.dem_sinh_vien()