class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Hoa: {self.name}, Màu sắc: {self.color}"

# Tạo đối tượng
flower1 = Flower("Hoa hồng", "Đỏ")

# In thông tin (tự động gọi __str__)
print(flower1)