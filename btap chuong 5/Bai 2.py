def read_and_process_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for index, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                numbers = list(map(int, line.split(",")))

                print(f"\nDòng {index}: {numbers}")
                negative_numbers = [num for num in numbers if num < 0]

                print(f"Số âm trong dòng {index}: {negative_numbers}")

    except FileNotFoundError:
        print("Không tìm thấy file!")
    except ValueError:
        print("Dữ liệu trong file không hợp lệ!")

read_and_process_file("numbers.txt")