# class Animal():
#     def __init__(self, name):
#         self.name = name
#     def sing(self):
#         print(self.name + ', can sing well')
    
# bird = Animal('phenix')
# print(bird.name)
# bird.sing()    

# class Animal(): #定義類別
#     def __init__(self, name):
#         slef.name = name #定義屬性
#     def sing(self): #定義方法
#         print(self.name + 'can sing very well') 

# # bird = Animal('phenix')  # 以類別建立物件
# # print(bird.name)
# # bird.sing()   

def div(a,b):
    return a/b
try:
    print(div(6,2))
    print(div(3,0))
except:
    ZeroDivisionError
    print(div(4,2))


