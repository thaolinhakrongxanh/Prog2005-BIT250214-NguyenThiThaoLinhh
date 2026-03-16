class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # class method tạo đối tượng từ chuỗi
    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))

    # hàm in thông tin
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


# Tạo đối tượng từ chuỗi
p = Person.from_string("Nam-20")

# In thông tin
print(p)