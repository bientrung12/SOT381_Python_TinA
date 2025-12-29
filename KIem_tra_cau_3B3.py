n=int(input("Nhập số lượng phần tử N: "))
a=[]
i=0
while i<n:
  x=int(input(f"Nhập phần tử thứ {i + 1}: "))
  a.append(x)
  i+=1
dem=0
print("Các số Armstrong trong danh sách là: ")
for x in a:
  if x>0:
    