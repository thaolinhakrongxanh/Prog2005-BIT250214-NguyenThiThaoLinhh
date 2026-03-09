def bai1():
    print("Đang chạy Bài 1")

def bai2():
    print("Đang chạy Bài 2")

def bai3():
    print("Đang chạy Bài 3")

def bai4():
    print("Đang chạy Bài 4")


while True:
    print("\n===== MENU =====")
    print("1. Chạy Bài 1")
    print("2. Chạy Bài 2")
    print("3. Chạy Bài 3")
    print("4. Chạy Bài 4")
    print("0. Thoát")

    choice = int(input("Nhập lựa chọn: "))

    if choice == 1:
        bai1()
    elif choice == 2:
        bai2()
    elif choice == 3:
        bai3()
    elif choice == 4:
        bai4()
    elif choice == 0:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")