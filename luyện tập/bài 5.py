class User:
    def __init__(self, id):
        self._id = id   # thuộc tính private

    @property
    def id(self):
        return self._id  # chỉ cho phép đọc


# Tạo đối tượng
u = User(101)

# Đọc id
print("User ID:", u.id)

# Thử thay đổi id
u.id = 200
