n=int(input("Nhập số lượng phần tử N: "))
a=[]
i=0
while i<n:
  x=int(input(f"Nhập phần tử thứ {i+1}: "))
  a.append(x)
  i+=1
tong=0
for x in a:
    if x%2==0 or x%3==0:
        tong+=x
print("Tổng các phần tử chia hết cho 2 hoặc 3 là:", tong)