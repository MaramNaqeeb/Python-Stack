


x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}

z = [ {'x': 10, 'y': 20} ]



# //1 update
x = [ [5,2,3], [10,8,9] ] 
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
print(x)


# //update
x = [ [5,2,3], [10,8,9] ] 
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print((z)[0])

# //update

students[0]['last_name']=["Bryant"]
print((students)[0])

# //update
sports_directory
sports_directory["soccer"][0]="Andres"
print(sports_directory)

# //3
for index in range(len(students)):
    for value in students[index]:
        print(students[index][value])
   
# //2
for dic in students:
    for key,val in dic.items():
        print(key,val)


   