'''
There are two arrays of numbers. the numbers are sorted in ascending order. 
Find the numbers that are common in both arrays. 
Eg - array 1 = [1,3,7,9,13,14], array2 [1,2,7,13,15]. answer - [1,7,13]
'''
#declaring the arrays
first_array=[]
second_array=[]

def getting_input_elements(): #function to get input from the user
    first_array_size=int(input("Enter the number of elements in the 1st array:")) #prompting the user the size of the array
    for item in range(0,first_array_size):
        input_item=int(input("Enter the element"+ str(item+1)+":")) #getting elements from the user 
        first_array.append(input_item)
    second_array_size=int(input("Enter the number of elements in the 2nd array:")) #prompting the user the size of the array
    for item in range(0,second_array_size):
        input_item=int(input("Enter the element"+ str(item+1)+":")) #getting elements from the user 
        second_array.append(input_item)

def common_elements(array1,array2): #function to find the common elements
    final_array = [value for value in array1 if value in array2] 
    return final_array

getting_input_elements()
array_with_common_elements=common_elements(first_array,second_array)
print("The common elements in both array:")
print(array_with_common_elements)

'''
Output:
Enter the number of elements in the 1st array:3
Enter the element1:1
Enter the element2:2
Enter the element3:3
Enter the number of elements in the 2nd array:4
Enter the element1:5
Enter the element2:3
Enter the element3:1
Enter the element4:2
The common elements in both array:
[1, 2, 3]
'''