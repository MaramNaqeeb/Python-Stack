# //Biggiie
def bigger_size(my_list):
    for i in range(0, len(my_list)):
        if my_list[i] > 0:
            my_list[i] = "big"
    return my_list
numbers = [1, -3, -4, -5, 6]
print(bigger_size(numbers))

# Count positives
def bigger_size(my_list):
    x = 0
    for i in range(0, len(my_list)):
        if my_list[i] > 0:
            x = x +1
    my_list[len(my_list)-1] = x
    return my_list
numbers = [1, -3, -4, -5,66,11]
print(bigger_size(numbers))

# //Sum Total
def sum_total(my_list):
    sum=0
    for i in my_list:
        sum=sum+i
    return sum  
print(sum_total([2,7,6,4]))

# Average
def average(my_list):
    sum=0
    for i in my_list:
        sum=sum+i
    average=sum/i
    return average  
print(average([2,7,6,4]))

# length
def length(my_list):
    for i in my_list:
        return len(my_list)
print(length([1,2,3,4]))

#minimum
def minimum(my_list):
    mini_value=my_list[0]
    for i in range(len(my_list)):
        if my_list[i]<mini_value:
            mini_value = my_list [i]
    return mini_value
print(minimum([3,5,1,7]))

def maximum(my_list):
    maxi_value=my_list[0]
    for i in range(len(my_list)):
        if my_list[i]>maxi_value:
            maxi_value = my_list[i]
    return maxi_value
print(maximum([4,1,8,7]))

# //reverse
def reverse(my_list):
    new_list=[]
    for i in range (len(my_list)-1,-1,-1):
        new_list.append(my_list[i])
    return new_list
print (reverse([1,2,3,4]))

# //ultimate_analysis
def ultimate_analysis(my_list):
    sumTotal = sum_total(my_list)
    minimum = minimum(my_list)
    maximum = maximum(my_list)
    average = average(my_list)
    length = length(my_list)

    my_dictionary = {
        "Sum": sum_total,
        "minimum":minimum,
        "maximum":maximum,
        "average": average,
        "length": length
    }
    return my_dictionary



    
   
    

     

    
            
            
            
