điểm_số =[8.5, 7.0, 6.0, 9.5, 5.2]
tổng_điểm = 0
số_môn = 0

print("Quá trình tính điểm")
for điểm in điểm_số:
    tổng_điểm += điểm
    số_môn += 1
    print(f"Môn {số_môn}; {điểm} điểm")

điểm_trung_bình = tổng_điểm / số_môn
print(f"Điểm trung bình: {điểm_trung_bình:.2f}")