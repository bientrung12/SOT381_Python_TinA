#bai1
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))

print("Tổng=", a+b+c)

#bai 2 viets pt nhập vào số nguyên cho biết số đố có đồng thời chia hết cho 3 và 5 hay không
number_str = input("Nhập một số nguyên: ")
number = int(number_str)
if number % 3 == 0 and number % 5 ==0:
    print(f"{number} là số chia hết cho 3 và 5.")
else:
  print(f"{number} là số không chia hết cho 3 và 5.")


  