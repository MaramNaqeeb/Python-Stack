# //countdown
def countdown(num):
    list = []
    for i in range (num, -1,-1):
         list.append(i)
    return list
print(countdown(10))
        

# //print and return
def print_and_return(arr):
    print (arr[0])
    return arr[1]
print (print_and_return ([10,5]))
           
# // first plus length
def first_plus_length (arr):
    first= arr[0]
    length=len(arr)
    return first+length
 
print(first_plus_length([5,7,2]))

# //values greater than second
def values_greater_than_second(arr):
    original_length=len(arr)
    if original_length<2:
        return False
    else:
     second_value=arr[1]
     new_arr=[]
     for i in arr:
        if i>second_value:
            new_arr.append(i) 
    print(len(new_arr))
    return new_arr
print (values_greater_than_second ([5,2,6,4,9,8]))


# //this length that value
def this_length_that_value(size,value):
    new_arr=[]
    for i in range(size):
        new_arr.append (value)
    return new_arr
print (this_length_that_value(4,7))