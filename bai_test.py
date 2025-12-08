#bai1
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
print("Tổng=", a+b+c)

#bai 2 viets pt nhập vào số nguyên cho biết số đố có đồng thời chia hết cho 3 và 5 hay không
n = int(input("Nhập một số nguyên: "))

if n % 3 == 0 and n % 5 == 0:
    print(f"{n} là số chia hết cho 3 và 5.")
else:
  print(f"{n} là số không chia hết cho 3 và 5.")


  