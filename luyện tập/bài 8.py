class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # nạp chồng toán tử +
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # in vector
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Tạo 2 vector
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Cộng 2 vector
v3 = v1 + v2

# In kết quả
print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector sau khi cộng:", v3)