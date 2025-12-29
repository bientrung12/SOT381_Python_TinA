n=int(input("Nhập số lượng phần tử N: "))
a=[]
i=0
while i<n:
  x=int(input(f"Nhập phần tử thứ {i+1}: "))
  a.append(x)
  i+=1
print("Các phần tử chia hết cho cả 2 và 3 là: ")
for x in a:
  if x%2==0 and x%3==0:
    print(x,end=" ")