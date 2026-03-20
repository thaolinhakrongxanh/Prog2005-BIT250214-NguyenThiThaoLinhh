# Import thư viện
import matplotlib.pyplot as plt

# Dữ liệu mẫu (Top 10 thành phố theo diện tích ở California - km2)
cities = [
    "Los Angeles", "San Diego", "California City", "San Jose",
    "San Francisco", "Fresno", "Sacramento", "Long Beach",
    "Oakland", "Bakersfield"
]

area_total_km2 = [1302, 964, 527, 469, 600, 298, 259, 133, 202, 390]

# Sắp xếp theo diện tích giảm dần
sorted_data = sorted(zip(area_total_km2, cities), reverse=True)
areas, city_names = zip(*sorted_data)

# Vẽ biểu đồ cột ngang
plt.barh(city_names, areas)

# Đảo ngược trục Y để thành phố lớn nhất nằm trên cùng
plt.gca().invert_yaxis()

# Tiêu đề và nhãn
plt.title("Top 10 thành phố lớn nhất California (theo diện tích)")
plt.xlabel("Diện tích (km²)")
plt.ylabel("Thành phố")

# Hiển thị giá trị trên mỗi cột
for i in range(len(areas)):
    plt.text(areas[i], i, f" {areas[i]}", va='center')

# Hiển thị
plt.show()