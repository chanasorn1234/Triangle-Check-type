## ฟังก์ชันเช็คชนิดตัวแปร
## ประกาศตัวแปร
triangular_side = list()

### รับตัวเลข (แบบทีเดียวแล้วเช็ค)
def check_type():
  inp = input("Enter Number : ").split()
  inp2 = []
  while len(inp) != 3:
    # print("LEN " , len(inp),inp)
    print("ไม่สามารถดำเนินการได้")
    inp = input("Enter Number Again : ").split()
  else:
    for i in range(0, len(inp)):
      try:
        int(inp[i])
        while int(inp[i]) <= 0: #check sub-zero
          print("ไม่สามารถดำเนินการได้ เนื่องจากมีด้านที่มีค่าน้อยกว่าหรือเท่ากับ 0") #ERROR NUMBER
          return check_type()
        inp2.append(inp[i])
      except ValueError:
        try:
          float(inp[i])
          while float(inp[i]) <= 0: #check sub-zero
            print("ไม่สามารถดำเนินการได้ เนื่องจากมีด้านที่มีค่าน้อยกว่าหรือเท่ากับ 0") #ERROR NUMBER
            return check_type()
          inp2.append(inp[i])
        except ValueError:
          print("ไม่สามารถดำเนินการได้ มีด้านที่มีค่าเป็น str")
          return check_type()
    return inp2

### หาประเภทสามเหลี่ยม
def find_triangular(triangular_side):
  if triangular_side[0] == triangular_side[1] == triangular_side[2]:
    print("Equilateral Triangle")
  elif (triangular_side[0] == triangular_side[1]) or (triangular_side[0] == triangular_side[2]) or (triangular_side[1] == triangular_side[2]):
    print("Isosceles triangle")
  elif ((pow(triangular_side[0],2) + pow(triangular_side[1],2)) == pow(triangular_side[2],2)) or ((pow(triangular_side[0],2) + pow(triangular_side[2],2)) == pow(triangular_side[1],2)) or ((pow(triangular_side[1],2) + pow(triangular_side[2],2)) == pow(triangular_side[0],2)):
    print("Right Triangle")
  else:
    print("Scalene Triangle")

## MAIN
while(1):
    triangular_side = list()
    num = check_type()
    for j in num:
        triangular_side.append(float(j))
    find_triangular(triangular_side)
# def check_type(i = None):
#     while True:
#         print("Enter Number [" , i, "] : ")
#         inp = input()
#         try:
#             num = int(inp)
#             break;
#         except ValueError:
#             try:
#                 num = float(inp)
#                 break;
#             except ValueError:
#                 print("ไม่สามารถดำเนินการได้") #ERROR TYPE
#     return num

##  ฟังก์ชันหาประเภทสามเหลี่ยม
def find_triangular(triangular_side):
    if triangular_side[0] == triangular_side[1] == triangular_side[2]:
        print("Equilateral Triangle")
    elif (triangular_side[0] == triangular_side[1]) or (triangular_side[0] == triangular_side[2]) or (triangular_side[1] == triangular_side[2]):
        print("Isosceles triangle")
    elif ((pow(triangular_side[0],2) + pow(triangular_side[1],2)) == pow(triangular_side[2],2)) or ((pow(triangular_side[0],2) + pow(triangular_side[2],2)) == pow(triangular_side[1],2)) or ((pow(triangular_side[1],2) + pow(triangular_side[2],2)) == pow(triangular_side[0],2)):
        print("Right Triangle")
    else:
        print("Scalene Triangle")

## ประกาศตัวแปร
# triangular_side = list()

## MAIN
### รับตัวเลข (แบบรับแล้วเช็คทีละตัว)
# for i in range(1, 4):
#   num = check_type(i)
#   while num <= 0:
#     print("ไม่สามารถดำเนินการได้") #ERROR NUMBER
#     num = check_type(i)
#   triangular_side.append(num)
# find_triangular(triangular_side)

