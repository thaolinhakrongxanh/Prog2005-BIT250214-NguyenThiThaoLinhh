class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # gọi constructor của lớp cha

    def sound(self):
        print("ha ha gâu gâu hi hi")  # ghi đè phương thức sound


# Tạo đối tượng Dog
dog1 = Dog("tên nó là chờ o cho sắc chó")

# Gọi phương thức
print("Tên con chó:", dog1.name)
dog1.sound()