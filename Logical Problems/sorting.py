'''
Sort the numbers in an array (ascending or descending).
'''
array=[] #Declaring the array
size=int(input("Enter the number of elements in the array:")) #prompting the user the size of the array
for item in range(0,size):
    input_item=int(input("Enter the element"+ str(item+1)+":")) #getting elements from the user 
    array.append(input_item)
for outer_loop in range(0,size): 
    for inner_loop in range(outer_loop+1,size):
        if array[outer_loop]>array[inner_loop]: #if a element is greter than its next element we are swapping it
            temp=array[outer_loop]
            array[outer_loop]=array[inner_loop]
            array[inner_loop]=temp
print(array)

'''
Output:
Enter the number of elements in the array:5
Enter the element1:5
Enter the element2:1
Enter the element3:2
Enter the element4:4
Enter the element5:3
'''