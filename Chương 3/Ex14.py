def count_vowels(s):
    vowels = "hello"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

s = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(s))