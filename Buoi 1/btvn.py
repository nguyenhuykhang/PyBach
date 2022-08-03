
'''-108, -86, -5, -1, 2, 3, 4, 7, 10, 15, 25, 30, 31, 45, 55'''
A = [2, 4, 3, 6, -108, 7, -5, -1, 10, 25, 28, 496, 15, -86, 30, 45, 31, 55]


'''1. Viết hàm tính giá trị trung bình các phần tử có giá trị dương trong mảng một chiều a có n phần tử. 
Hàm trả về giá trị trung bình của các phần tử có giá trị dương. Ngược lại hàm trả về giá trị 0 '''
def tbduong(A):
    m = 0
    n = 0
    for x in A:
        if x > 0:
            m = m + x
            n = n + 1
    if n == 0:
        print ("Khong co gia tri trung binh")
    else:
        trung_binh = m/ n
        print("Gia Tri trung binh cac phan tu duong la: ", trung_binh)


'''2. Viết hàm tính giá trị trung bình các số nguyên tố trong mảng một chiều a có n phần tử. 
Hàm trả về giá trị trung bình của các phần tử là số nguyên tố. Ngược lại hàm trả về giá trị 0.'''


'''def tbnguyento(A):
    if 2 in A:
        s = 1
        sum = 2
        for x in A:
            if x > 2:
                for y in range(2, x):
                    if (x % y) == 0:
                        break;
                else:
                    sum = sum + x
                    s = s + 1
        trung_binh = sum / s
        print("Gia Tri trung binh cac phan tu nguyen to la: ", trung_binh)
    else:
        s = 0
        sum = 0
        for x in A:
            if x > 2:
                for y in range(2, x):
                    if (x % y) == 0:
                        break;
                else:
                    sum = sum + x
                    s = s + 1
        trung_binh = sum / s
        print("Gia Tri trung binh cac phan tu nguyen to la: ", trung_binh)'''

'''CHUA BAI'''

def tb_nguyen_to(A):
    tong = 0
    dem = 0
    for x in A:
        if check_nguyen_to(x):
            tong += x
            dem += 1
    if dem == 0:
        return 0
    tb = tong / dem
    print("trung binh nguyen to la: ", tb)

def check_nguyen_to(x):
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

'''3. Viết hàm tính giá trị trung bình các số hoàn hảo trong mảng một chiều a có n phần tử. 
Hàm trả về giá trị trung bình của các phần tử là số hoàn hảo. Ngược lại hàm trả về giá trị 0.'''


def sohoanhao(A):
    sum = 0
    chia = 0
    for x in A:
        cong = 0
        for i in range(1, x):
            if (x % i == 0):
                cong += i
        if x == cong:
            sum += x
            chia += + 1

    print("Gia tri trung binh cac so hoan hao la: ", sum / chia)


'''4. Viết hàm tính giá trị trung bình các số chẵn và chia hết cho 3 trong mảng một chiều a có n phần tử. 
Hàm trả về giá trị trung bình của các phần tử thỏa mãn. Ngược lại hàm trả về giá trị 0.'''


def sochan3(A):
    sum = 0
    s = 0
    for x in A:
        if (x % 2) == 0 and (x % 3 == 0):
            sum = sum + x
            s = s + 1
    trung_binh = sum / s
    print("Gia Tri trung binh cac phan tu so le chia het cho 3 la: ", trung_binh)


'''5. Viết hàm tính giá trị trung bình các số lẻ và chia hết cho 5 trong mảng một chiều a có n phần tử. 
Hàm trả về giá trị trung bình của các phần tử thỏa mãn. Ngược lại hàm trả về giá trị 0.'''


def sole5(A):
    sum = 0
    s = 0
    for x in A:
        if (x % 2) == 1:
            if x % 5 == 0:
                sum = sum + x
                s = s + 1
    trung_binh = sum / s
    print("Gia Tri trung binh cac phan tu so le chia het cho 5 la: ", trung_binh)


'''6. Viết hàm sắp xếp mảng a có n phần tử theo thứ tự tăng dần.'''


def xep(A):
    T = []
    for i in range(1, len(A) + 1):
        nho_nhat = min(A)
        T.append(min(A))
        A.remove(nho_nhat)
    print("Cac phan tu co gia tri tang dan: ", T)


if __name__ == '__main__':
    tbduong(A)
    tb_nguyen_to(A)

    sohoanhao(A)
    sochan3(A)
    sole5(A)
    xep(A)
