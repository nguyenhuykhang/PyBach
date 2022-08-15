class SinhVien:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def lay_ten(get_name):
      return get_name.name
  def lay_tuoi(get_age):
      return get_age.age
  def get_all(all):
      return all.name, all.age

def add(num1, num2):
    num = num1 + num2
    return num
return_val = add(300, 500)
print(return_val)

class SoHoc:
    def __init__(self, number1, number2):
        self.first_num = number1
        self.second_num = number2
    def __init__(self):
        self.first_num = 5
        self.second_num = 10
    def getall(lay):
        return lay.first_num, lay.second_num
    def set_all(self, num1, num2):
        self.first_num = num1
        self.second_num = num2
    def inputInfo(self):
        self.first_num = int(input("Nhap so thu nhat: "))
        self.second_num = int(input("Nhap so thu hai: "))




class Vector:
    def __init__(self, par_x, par_y):
        self.x = par_x
        self.y = par_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __eq__(self, v):
        rd = self.x == v.get_x() and self.y == v.get_y()
        return rd


if __name__ == '__main__':
    # p1 = SinhVien("Tuan", 18)
    # print(p1.lay_ten())
    # print(p1.lay_tuoi())
    # person_name, person_age = p1.get_all()
    # print("{}, {}".format(person_name,person_age))
    # new = SoHoc(11, 1)
    # first_number, second_number = new.getall()
    # print("GET {}, {}".format(first_number, second_number))
    # new.set_all(30, 13)
    # firs_new_number, second_new_number = new.getall()
    # print("{}, {}".format(firs_new_number, second_new_number))
    # sohoc = SoHoc()
    # sohoc.inputInfo()
    # first_number, second_number = sohoc.getall()
    # print("{}, {}".format(first_number, second_number))
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    rs = v2.__eq__(v1)
    print(rs)










