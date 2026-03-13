def diem_trung_binh(students):
    tong = sum(students.values())
    so_luong = len(students)
    return tong/so_luong


students = {"ha":8.4,"nhat":8.2,"linh":8.5}
print("Diem trung binh:", diem_trung_binh(students))

