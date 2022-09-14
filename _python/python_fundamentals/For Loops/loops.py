# //first
for i in range(0,151):
    print(i)
# //second
for i in range(5,1001,5):
    print(i)
# //third
for i in range(1,101):
   if (i % 10 == 0):
       print("Coding Dojo")
   elif (i % 5 == 0):
       print("Coding")
   else:
      print(i)

# //forth
my_result=0
for i in range(0,500001):
    my_result+=i;
    my_result=my_result+i
    # i++
    # i=i+1
    # i+=1
print(my_result)


# //fifth
for i in range(2018,0,-4):
   print(i)


# //sixth
lowNum=1
highNum=20
mult=3
for i in range(3,20,3):
 print (i) 

# method 2
low = 1
high = 40
multi = 4
for i in range (low,high):
    if i%3 == 0:
        print (i)
