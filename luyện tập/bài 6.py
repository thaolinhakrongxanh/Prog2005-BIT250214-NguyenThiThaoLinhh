class Product:
    def __init__(self, price):
        self._price = price   # khởi tạo giá

    # getter
    @property
    def price(self):
        return self._price

    # setter
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải lớn hơn 0")

    # hàm in thông tin
    def __str__(self):
        return f"Giá sản phẩm: {self._price}"


# Khởi tạo đối tượng
p = Product(100)

# In thông tin product
print(p)

# In riêng giá
print("Price:", p.price)