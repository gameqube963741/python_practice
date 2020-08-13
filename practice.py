# def GetArea(width, height):
#     area = width * height
#     return area

# ret1 = GetArea(6,9) #ret1 = 54
# print(ret1)

def Circle(radius):
    area = radius * radius * 3.14
    length = 2 * radius * 3.14
    return area, length 
area1, length1 = Circle(5)
print(Circle(5))