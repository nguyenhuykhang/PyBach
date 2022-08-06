A = [-5, 2, 3, 5, 6, 28, 496, 11, 16, 37, 41, 103]
# Bai 1: Cho mảng số nguyên sau đó ghi nhưng phần tử của mảng là số nguyên tố file txt với che do write
def in_nguyen_to(A):
    tong = 0
    for x in A:
        if check_nguyen_to(x):
            tong += x
            f = open("new_file.txt", "w")
            f.write(str(x))
            f.close()
            f = open("new_file.txt", "r")
            print(f.read())
    return tong


def check_nguyen_to(x):
    if x > 0:
        if x == 2:
            return True
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


# Bai 2 In ra tổng số hoàn hảo trong file
def check_so_hoan_hao(x):
    if x > 0:
        tong = 0
        for i in range(1, x):
            if (x % i) == 0:
                tong += i
        if x == tong:
            return True
        else:
            return


def in_hoan_hao(A):
    sum = 0
    for x in A:
        if check_so_hoan_hao(x):
                sum = sum + x
    f = open("so_hoan_hao_file.txt", "w")
    f.write(str(sum))
    f.close()
    f = open("so_hoan_hao_file.txt", "r")
    print("Tong cac so hoan hao la: ", f.read())

def input_tu():
    while True:
        B = input(str("Nhap mot cum tu: "))
        if B == "exit":
            break
        else:
            them_tu = open("file_tu.txt", "a", encoding="utf-8")
            them_tu.write(B)
            them_tu.close()
            them_tu = open("file_tu.txt", "r", encoding="utf-8")
            print(them_tu.read())
# File Bài 1: Nhập vào một chuỗi ký tự, xuất ra màn hình chuỗi bị đảo ngược thứ tự các ký tự. Sau đó viết 1 hàm ghi lại vào file
def dao_nguoc():
    nhap = input("Nhap tu ban muon dao nguoc: ")
    ghi_file = str(nhap)[::-1]
    f = open("file_dao_nguoc.txt", "w")
    f.write(ghi_file)
    f.close()
    f = open("file_dao_nguoc.txt", "r")
    print("Tu dao nguoc ghi vao file la:", f.read())


# File Bài 3: Nhập xâu ký tự từ bàn phím, ghi ra từ dài nhất trong xâu (từ là dãy ký tự không chứa ký tự trắng) vào file tu_dai_nat.txt
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

# File Bài 2. Viết chương trình nhập dữ liệu từ bàn phím và đổi những ký tự đầu tiên của mỗi từ thành chữ in hoa vào file: chuan_hoa.txt
def in_hoa_chu_dau():
    nhap = input("Nhap tu de in hoa chu cai dau: ")
    arr = []
    tach = nhap.split()
    for x in tach:
        arr.append(x.capitalize())
    new = " ".join(arr)
    f = open("chuan_hoa.txt", "w")
    f.write(new)
    f.close()
    f = open("chuan_hoa.txt", "r")
    print("In hoa chu cai dau ghi vao file la:", f.read())


if __name__ == '__main__':
    x = in_nguyen_to(A)
    print("Tong cac so nguyen to: ", x)
    # a ="1777765667576980"
    # x = int(a)
    # print(type(x))
    in_hoan_hao(A)
    in_hoa_chu_dau()
    dai_nhat()
    dao_nguoc()
    input_tu()


