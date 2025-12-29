n=int(input("Nhập số lượng bài hát: "))
dsBaiHat=[]
for i in range(n):
  tenBai=input("Tên bài thứ {i+1}")
  dsBaiHat. append (tenBai)

for i in range(n):
  ten=dsBaiHat[i]
  print( "Bài {i}: {ten)")
for bai in dsBaiHat:
 print("bai",i+1,ten)