x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# # Update value in dictionaries and lists

def updateValue():
    x[1][0] = 15
    students[0]['last_name'] = "Bryant"
    sports_directory['soccer'][0] = 'Andres'
    z[0]['y'] = 30

updateValue()
print(x)
print(students)
print(sports_directory)
print(z)


# Iterate through a list of dictionaries

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for keys in some_list:
        print(keys)

# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# get vakues from a list of dictionaries 
def iterateDictionary2(key_name, some_list):
    for listItem in some_list: 
        print(listItem[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    locations = len(some_dict['locations'])
    instructors = len(some_dict['instructors'])
    print(locations , 'LOCATIONS')
    for values in some_dict['locations']:
        print(values)
    print(instructors , 'INSTRUCTORS')
    for values in some_dict['instructors']:
        print(values)

printInfo(dojo)






# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
