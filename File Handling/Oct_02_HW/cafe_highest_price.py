
file=open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\input_cafe.csv","r") #opening the csv file in reading mode
file_line=file.readline() #reading single line from the file
maxlist=[]
while file_line:
    linelist=file_line.split(",") #converting the line into list
    price=linelist[2] #seperating and storing the values from the selling_price column
    pricelist=price.split("\n") #converting the values into list
    file_line=file.readline()
    for index in pricelist: #storing only the numeric values
        if index.isnumeric():
            maxlist.append(index)
print("Maximum price is:",max(maxlist, key=lambda value: int(value)) )

'''
Output:
Maximum price is: 200
'''