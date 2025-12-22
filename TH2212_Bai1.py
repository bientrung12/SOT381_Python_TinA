while True:
  w=float(input("Nhập chiều dài hình chữ nhật: "))
  h=float(input("Nhập chiều rộng hình chữ nhật: "))

  if (w>=0.0) and (h<=100.0):
      break
  else:
      print("Nhập sai dữ liệu vui lòng nhập lai")
Chu_vi= (w+h)*2
Dien_tich= w*h
print(f"Chu vi hình chữ nhật là {Chu_vi:.2f}")
print(f"Diện tích hình chữ nhật là {Dien_tich:.2f}")
 

