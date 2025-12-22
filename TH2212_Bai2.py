a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
min = a
if b< min:
    min = b
if c < min:
    min = c
print(f"Số lớn nhất là {max}")
print(f"Số nhỏ nhất là {min}")