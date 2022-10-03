
file=open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\input_cafe.csv","r") #opening the csv file in reading mode
file_line=file.readline() #reading single line from the file
maxprice=0
maxlist=[]
while file_line:
    linelist=file_line.split(",") #converting the line into list
    price=linelist[2] #seperating and storing the values from the selling_price column
    pricelist=price.split("\n") #converting the values into list
    file_line=file.readline()
    for index in pricelist: #storing only the numeric values
        if index.isnumeric():
            maxlist.append(index)
for max_value in maxlist: #finding the maximum value
    if int(max_value) > int(maxprice):
        maxprice=max_value
print("Maximum price is:",maxprice)

'''
Output:
Maximum price is: 200
'''