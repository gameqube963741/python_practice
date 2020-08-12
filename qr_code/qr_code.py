import qrcode
#二維條碼內容
data = "https://balatutu.com/"
#生成二維條碼
img = qrcode.make(data=data)
#顯示二維條碼
img.show()
# 保存條碼
# img.save(Qr.png)
print('Qrcode OK')