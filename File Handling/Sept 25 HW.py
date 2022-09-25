file1=open('C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\read_file.txt','r')
file2=open('C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\write_file.txt','w')
for letter in file1:
    file2.write(letter)
file1.close()
file2.close()