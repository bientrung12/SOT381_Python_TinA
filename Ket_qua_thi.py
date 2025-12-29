Toan=float(input("Nhập điểm môn Toán: "))
Ly=float(input("Nhập điểm môn Lý: "))
Hoa=float(input("Nhập điểm môn Hóa: "))
Tong= Toan + Ly + Hoa
if Tong >=15 and Toan>=4 and Ly>=4 and Hoa>=4:
    print("Kết quả đậu");
    if Toan>5 and Ly>5 and Hoa>5:
       print("Học đều các môn")
    else:
       print("Học chưa đều các môn")
else:
      print("Thi hỏng")