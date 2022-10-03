file=open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\output_cafe.csv","r")
fileline=file.readline() #reading single line from the file
while fileline:
    linelist=fileline.split(",")
    fileline = file.readline()
    print(linelist)# use readine() to read next line
file.close()

'''
Output:
['Item_name', 'Quantity_Sold', 'Profit', 'Loss', 'Remaining_stock\n']
['Vadai', '0', '0', '0', '100\n']
['Pizza', '0', '0', '0', '50\n']
['Coke', '0', '0', '0', '100\n']
['Burger', '0', '0', '0', '30\n']
['Sandwich', '0', '0', '0', '50\n']
'''