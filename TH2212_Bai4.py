def so_LN_NN(a,b,c):
  LN=a 
  if b>LN:
    LN = b
  if c>LN:
    LN = c
  NN=a
  if b<NN:
      NN = b
  if c<NN:
      NN = c
  return LN,NN

a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
nummax, nummin = so_LN_NN(a,b,c)
print(f"Số lớn nhất là {nummax}")
print(f"Số nhỏ nhất là {nummin}")
