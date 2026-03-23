# Hàm nhập ma trận
def nhap_ma_tran(rows, cols, ten):
    matrix = []
    print(f"\nNhập ma trận {ten}:")

    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                value = input(f"Nhập phần tử [{i}][{j}]: ")

                # Kiểm tra nhập trống
                if value.strip() == "":
                    print("❌ Không được để trống! Nhập lại.")
                else:
                    row.append(float(value))  # ép sang số
                    break
        matrix.append(row)

    return matrix


# Nhập kích thước ma trận
rows = int(input("Nhập số dòng: "))
cols = int(input("Nhập số cột: "))

# Nhập 2 ma trận
A = nhap_ma_tran(rows, cols, "A")
B = nhap_ma_tran(rows, cols, "B")

# Cộng ma trận
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# In kết quả
print("\nMa trận kết quả (A + B):")
for row in C:
    print(row)