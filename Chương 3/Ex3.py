colors = ["Red", "Blue", "Green", "Yellow", "Pink"]

try:
    colors.remove("Green")
    print("Sau khi xóa Green:", colors)
except ValueError:
    print("Không tìm thấy Green trong danh sách!")