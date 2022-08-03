thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"model" : "Focus"})

print(thisdict)

sinh_vien = {
    "nguoi_1": "Bach",
    "nguoi_2": "Tuan",
    "nguoi_3": "Tuan",
    "nguoi_4": "Huyen",
    "nguoi_5": "Khang",
    "nguoi_6": "Tuan"
}

for i in range(1, len(sinh_vien) + 1):
    if sinh_vien["nguoi_" + str(i)] == "Tuan":
        sinh_vien["nguoi_" + str(i)] = "Tuan 1"
print(sinh_vien)

'''for x in sinh_vien.keys():
    if sinh_vien[x] == "Tuan":
        # sinh_vien.[x] = "Tuan 1"
        sinh_vien.update({x : "Tuan 1"})
print(sinh_vien)'''

# ten = "Ha Anh Tuan"
# Bai 1: Viết hàm đầu vào 1 chuỗi. Hàm này trả về chuỗi đảo ngược thứ tự các ký tự
print("Dao nguoc ky tu:", "Ha Anh Tuan"[::-1])

# Bai 2: Đếm xem trong chuỗi xem có ký tự nào xuất hiện nhiều nhất.


'''Bai 3: In ra từ dài nhất trong chuỗi (từ là dãy ký tự không chứa ký tự trắng).
chia_ten = ten.split()
max = len(chia_ten[0])
for i in chia_ten:
    if len(i) >= max:
        max = len(i)
print("Tu dai nhat la: ", i)'''




ten = "ha anh tuan"
# Bai 4:
arr = ten.split()
chuyen = []
for i in arr:
    chuyen.append(i.capitalize())
print(" ".join(chuyen))


















