def so_lon_nhat(a,b,c):
  LN=a 
  if b>LN:
    LN = b
  if c>LN:
    LN = c
  return LN

a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
nummax = so_lon_nhat(a,b,c)
print(f"Số lớn nhất là {nummax}")
