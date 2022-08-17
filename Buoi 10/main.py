x = 34
def f1():
    global x
    x = 100
print(x)
class Student():
    def __init__(self, id, gpa, age, stu_class):
        self.masv = id
        self.diemtb = gpa
        self.tuoi = age
        self.lop = stu_class
        # if len(ID) != 8:
        #     raise Exception("Ma sinh vien khong hop le")
        # self.masv = ID
        # if not 0 <= GPA <= 10:
        #     raise Exception("Diem trung binh khong hop le")
        # self.diemtb = GPA
        # if not age >= 18:
        #     raise Exception("Tuoi khong hop le")
        # self.tuoi = age
        # if not stu_class[0] == "A" or stu_class[0] == "C":
        #     raise Exception("Lop khong hop le")
        # self.lop = stu_class

    def __inputInfo__(self):
        self.masv = input("Nhap ma sinh vien: ")
        while True:
            # self.masv = input("Nhap ma sinh vien: ")
            if len(self.masv) == 8:
                break
            elif len(self.masv) != 8 :
                self.masv = input("Nhap ma sinh vien: ")

        self.diemtb = float(input("Nhap diem trung binh sinh vien: "))
        while True:
            # self.diemtb = float(input("Nhap diem trung binh sinh vien: "))
            if 0 <= self.diemtb <10:
                break
            else:
                self.diemtb = float(input("Nhap lai diem trung binh: "))


        self.tuoi = int(input("Nhap tuoi sinh vien: "))
        while True:
            if self.tuoi >= 18:
                break
            else:
                self.tuoi = int(input("Nhap tuoi sinh vien: "))

        self.lop = (input("Nhap lop cua sinh vien: "))
        while True:
            # self.lop = (input("Nhap lop cua sinh vien: "))
            if self.lop[0] == "A" or self.lop[0] == "C":
                break
            else:
                self.lop = input("Nhap lop sinh vien: ")

    def __showInfo__(self):
        print(self.masv, self.diemtb, self.tuoi, self.lop)


if __name__ == '__main__':

        sv = Student("","" ,"" , "")
        sv.__inputInfo__()
        print(sv.__showInfo__())


