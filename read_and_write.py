# # file = open ('data.txt','w', encoding='utf-8-sig')
# # file.write('中文測試')
# # file.close()


# # 讀取檔案
# # 讀取每一行資料並加總
# # with open('data.txt','r',encoding='utf-8-sig') as file:
# #     sum=0
# #     for line in file:
# #         sum += int(line)
# #     print(sum)


# # 使用 JSON 格式讀取、複寫檔案
# import json
# with open('config.json','r') as file:
#     data = json.load(file)

# print(data)
# print('name:',data['name'])
# print('version:',data['version'])

# # 更新的資料
# data["name"]="NEW NAME"

# # 把最新的資料複寫到檔案中
# with open('config.json','w') as file:
#     json.dump(data, file)