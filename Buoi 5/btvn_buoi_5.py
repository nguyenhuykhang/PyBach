# Bai 1 Viết hàm nhập vào một số nguyên x gồm ba chữ số và xuất ra màn hình chữ số lớn nhất ở vị trí nào?
# Ví dụ: x = 291. Chữ số lớn nhất là 9 nằm ở hàng chục.
def max_vitri():
    nhap = int(input("Nhap so x gom ba chu so: "))
    tach = list(str(nhap))
    max = 0
    for idx, i in enumerate(tach):
        if int(i) > max:
            max = int(i)
            t = idx
    print("Chu so lon nhat la: ", max)
    if t == 0:
        print("Va o vi tri hang tram")
    elif t == 1:
        print("Va o vi tri hang chuc")
    elif t == 2:
        print("Va o vi tri hang don vi")


# Bai 2 Viết hàm nhập vào số nguyên x gồm ba chữ số và xuất ra màn hình theo thứ tự tăng dần của các chữ số.
# Ví dụ: x = 291. Xuất ra 129.
def thu_tu_tang_dan():
    nhap = int(input("Nhap so x gom 3 chu so: "))
    tach = list(str(nhap))
    arr = []
    for i in range(1, len(tach) + 1):
        nho_nhat = min(tach)
        arr.append(nho_nhat)
        tach.remove(min(tach))
    print("Thu tu tang dan cua cac chu so la: ", "".join(arr))

# Bai 3. Viết hàm nhập vào một tháng m hợp lệ và cho biết tháng đó có bao nhiêu ngày?
def month():
    nhap = int(input("Nhap vao 1 thang trong nam: "))
    while not 0 < nhap <= 12:
        nhap = int(input("Khong hop le, nhap vao 1 thang trong nam: "))
    thang_31 = [1, 3, 5, 7, 8, 10, 12]
    thang_30 = [4, 6, 9, 11]

    if nhap == 2:
        print("Thang", nhap, "co 29 ngay")
    elif nhap in thang_31:
        print("Thang", nhap, "co 31 ngay")
    elif nhap in thang_30:
        print("Thang", nhap, "co 30 ngay")




# Bai 4. Viết hàm nhập số nguyên dương k. Liệt kê k số nguyên tố đầu tiên.
def check_nguyen_to(x):
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def liet_ke_nguyen_to():
    k = int(input("Nhap so nguyen duong k de liet ke nguyen to: "))
    arr = []
    dem = 1
    x = 2
    while dem <= k:
        if check_nguyen_to(x):
            arr.append(x)
            dem += 1
        x += 1
    print(k,"so nguyen to dau tien la: ", arr)

# Bai 5 Viết hàm nhập vào hai số nguyên dương x và y. Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của x và y.
def ucln_bcnn():
    x = int(input("Nhap so nguyen duong x: "))
    y = int(input("Nhap so nguyen duong y: "))
    arr = []
    start = 1
    dem = 1
    if y <= x:
        while start <= y:
            if (x % start == 0) and (y % start == 0):
                arr.append(start)
            start += 1
        print(arr)
        uscln = arr[-1]
        print("Uoc chung lon nhat cua x va y la: ", uscln)
        bscnn = x*y/uscln
        print("Boi chung nho nhat cua x va y la: ", bscnn)
    elif x <= y:
        while start <= x:
            if (x % start == 0) and (y % start == 0):
                arr.append(start)
            start += 1
        print(arr)
        uscln = arr[-1]
        print("Uoc chung lon nhat cua x va y la: ", uscln)
        bscnn = x * y / uscln
        print("Boi chung nho nhat cua x va y la: ", bscnn)



# Bai 8 Viết hàm tìm các số hoàn hảo nhỏ hơn hoặc bằng k với k nhập từ bàn phím.
def check_hoan_hao(x):
    cong = 0
    for i in range(1, x):
        if x % i == 0:
            cong += i
    if x == cong:
        return True

def so_hoan_hao_k():
    arr = []
    dem = 1
    k = int(input("Nhap so nguyen duong k de tim so hoan hao: "))
    x = 6
    while dem <= k:
        if check_hoan_hao(x):
            arr.append(x)
            dem += 1
        x += 1
    print(arr)


# Bai 9 Viết hàm liệt kê các số phong phú trong đoạn [L, R]. L, R <= 105.
# 1 + 2 + 3 + 4 + 6 = 16 > 12.
# Ví dụ: [L, R] = [1, 50] Từ 1 đến 50 có 9 số phong phú là: 12, 18, 20, 24, 30, 36, 40, 42, 48.
def so_phong_phu():
    be = int(input("Nhập khoảng chặn dứoi: "))
    lon = int(input("Nhập khoảng chặn trên: "))
    arr = []
    for x in range(be, lon + 1, 1):
        cong = 0
        for i in range(1, x):
            if (x % i == 0):
                cong = cong + i
        if cong > x:
            arr.append(x)
    print("Tu", be, "den", lon, "co", len(arr), "so phong phu" ,arr)


# Bai 10. Số tam hoa: Viết hàm tìm các số nguyên gồm 3 chữ số sao cho tích của 3 chữ số bằng tổng 3 chữ số. Ví dụ: 1*2*3 = 1+2+3.
def tam_hoa():
    # nhap = (input("Nhap so co 3 chu so de kiem tra so tam hoa: "))
    arr = []
    # tach = list(nhap)
    for i in range(100, 1000):
        cong = 0
        nhan = 1
        t = list(str(i))
        for x in t:
            cong += int(x)
            nhan = nhan*int(x)
        if cong == nhan:
            arr.append(i)
    print("So tam hoa co 3 chu so la: ", arr)

# Bai 11 Viết hàm tìm tất cả các số nguyên tố trong đoạn [L, R] .
def nto_trong_doan():
    be = int(input("Nhập khoảng chặn dứoi: "))
    lon = int(input("Nhập khoảng chặn trên: "))
    arr = []
    for x in range(be, lon + 1):
        if check_nguyen_to(x):
            arr.append(x)
    print("Cac so nguyen to trong khoang tu", be, "den", lon, "la: ", arr)
def check_nguyen_to(x):
        if x == 1:
            return False
        if x == 2:
            return True
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

# Bai 12 Viết hàm tính số hạng thứ k của dãy Fibonaci.
# Dãy Fibonaci là dãy số gồm các số hạng F(k) với: F(k) = F(k-1) + F(k-2) với k>2 và F(1) = F(2) = 1.
def k_fibonaci():
    k = int(input("Nhap so k de tim so fibonaci: "))
    dem = 1
    if k == 1 or k == 2:
        print("So hang thu", k, "cua day fibonaci la 1")
    if k >2:


if __name__ == '__main__':
    k_fibonaci()
    nto_trong_doan()
    tam_hoa()
    so_phong_phu()
    ucln_bcnn()
    so_hoan_hao_k()
    liet_ke_nguyen_to()
    month()
    thu_tu_tang_dan()
    max_vitri()