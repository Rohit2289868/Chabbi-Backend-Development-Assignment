filename = ["abc.jpg", "xyz.xls", "text.csv", "123", "text.png"]
dic = {}

for x in filename:
    if x.find("jpg") != -1:
        dic[x] = "image"
    
    elif x.find("png") != -1:
        dic[x] = "image"
    
    elif x.find("xls") != -1:
        dic[x] = "Spreadsheet"
    
    elif x.find("xlsx") != -1:
        dic[x] = "Spreadsheet"
    
    else:
        dic[x] = "unknown"

print(dic)