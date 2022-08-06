# File Bài 1: Nhập vào một chuỗi ký tự, xuất ra màn hình chuỗi bị đảo ngược thứ tự các ký tự. Sau đó viết 1 hàm ghi lại vào file
def dao_nguoc():
    nhap = input("Nhap tu ban muon dao nguoc: ")
    ghi_file = str(nhap)[::-1]
    f = open("file_dao_nguoc.txt", "w")
    f.write(ghi_file)
    f.close()
    f = open("file_dao_nguoc.txt", "r")
    print("Tu dao nguoc ghi vao file la:", f.read())


# File Bài 2: Nhập xâu ký tự từ bàn phím, ghi ra từ dài nhất trong xâu (từ là dãy ký tự không chứa ký tự trắng) vào file tu_dai_nat.txt
def dai_nhat():
    nhap = input("Nhap tu de xac dinh dai nhat: ")
    arr = nhap.split()
    max = ""
    for x in arr:
        if len(x) > len(max):
            max = x
    f = open("tu_dai_nhat.txt", "w")
    f.write(str(max))
    f.close()
    f = open("tu_dai_nhat.txt", "r")
    print("Tu dai nhat ghi vao file la:", f.read())

# File Bai 4 Viết chương trình đếm có bao nhiêu khoảng trắng trong chuỗi. Ghi ra "Số lần xuất hiện khoảng trắng ra file: " ra count_space.txt
def dem_khoang_trang():
    nhap = input(str("Nhap tu de dem khoang trang"))
    tach = list(nhap)
    dem = 0
    for x in tach:
        if x == " ":
            dem += 1
    f = open("count_space.txt", "w")
    f.write(str(dem))
    f.close()
    f = open("count_space.txt", "r")
    print("So khoang trang la:", f.read())


# Bài 8. Viết chương trình nhập vào một chuỗi, hãy loại bỏ những khoảng trắng thừa trong chuỗi và ghi ra nội dung vào file: remove_space.txt
def loai_khoang_trang():
    nhap = input(str("Nhap tu de loai khoang trang: "))
    nhap.strip()
    x = nhap.replace("  ", " ")
    print(x)


# Viết chương trình nhập vào 2 chuỗi s1 và s2, nối chuỗi s2 vào s1. Xuất chuỗi s1 ra màn hình và ghi vào file concat_string.txt
def noi_chuoi():
    nhap1 = input("Nhap chuoi 1: ")
    nhap2 = input("Nhap chuoi 2: ")
    nhap1 = nhap1 + " " + nhap2
    f = open("concat_string.txt", "w")
    f.write(str(nhap1))
    f.close()
    f = open("concat_string.txt", "r")
    print("Chuoi sau khi noi la:", f.read())

# Bài 10. Viết chương trình tìm kiếm một ký tự xem có trong chuỗi hay không, nếu có xuất ra vị trí của từ đó.
def tim_kiem():
    chuoi = "Ha Anh Tuan"
    nhap = input(str("Nhap ky tu ban muon kiem tra: "))
    for idx, i in enumerate(chuoi):
        if i == nhap:
            print("Co ky tu", i, "trong chuoi va o vi tri", idx)
    else:
        print("Khong co!")



if __name__ == '__main__':
    tim_kiem()
    loai_khoang_trang()
    noi_chuoi()
    # loai_khoang_trang()
    dao_nguoc()
    dai_nhat()
    dem_khoang_trang()
