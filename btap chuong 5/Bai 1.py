import os
FILE_NAME = "products.txt"
def add_product():
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")

    try:
        price = float(input("Nhập giá: "))
    except ValueError:
        print("Giá phải là số!")
        return

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")

    print("Thêm sản phẩm thành công!")
def read_products():
    products = []

    if not os.path.exists(FILE_NAME):
        return products

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 3:
                code, name, price = parts
                products.append({
                    "code": code,
                    "name": name,
                    "price": float(price)
                })

    return products
def display_products(products):
    if not products:
        print("Danh sách trống!")
        return

    print("\nDanh sách sản phẩm:")
    for p in products:
        print(f"{p['code']} | {p['name']} | {p['price']}")
def sort_by_price_desc():
    products = read_products()
    products.sort(key=lambda x: x["price"], reverse=True)

    print("\nDanh sách sau khi sắp xếp giảm dần theo giá:")
    display_products(products)
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Nhập sản phẩm")
        print("2. Hiển thị danh sách sản phẩm")
        print("3. Sắp xếp theo giá giảm dần")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            products = read_products()
            display_products(products)
        elif choice == "3":
            sort_by_price_desc()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()