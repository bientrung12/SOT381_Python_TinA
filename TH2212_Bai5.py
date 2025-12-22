def tinh_S(n):
    tu_so = 0
    mau_so = 0
    i = 1
    while i <= n:
        tu_so += i
        i += 1
    i = 2
    while i <= n:
        mau_so += i
        i += 2
    return tu_so / mau_so
while True:
    n = int(input("Nhập số n: "))
    if n > 0 and n % 2 == 0:
        break

S = tinh_S(n)
print(f"Đáp án là {S:.2f}")