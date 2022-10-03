file=open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\output_cafe.csv","r")
fileline=file.readline() #reading single line from the file
while fileline:
    linelist=fileline.split(",")
    fileline = file.readline()
    print(linelist)# use readine() to read next line
file.close()