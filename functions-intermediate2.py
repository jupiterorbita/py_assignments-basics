# Assignment: Functions Intermediate II
# Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.

# 1. Update Values in Dictionaries and Lists
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
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)







# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
  for n in range(0,len(students),1):
    print(f'{n+1}. First_name = {students[n]["first_name"]}, Last_name = {students[n]["last_name"]}')

iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel





# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
def iterateDictionary2(key_name, some_list):
  for n in range(len(some_list)):
    # print(n, some_list[n])
    print(some_list[n][key_name])
  print()
  return

iterateDictionary2('first_name', students)
# Michael
# John
# Mark
# KB

iterateDictionary2('last_name', students)
# # And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel



# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
print('='*60)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dicto):
  for key, value in some_dicto.items():
    print("{} {}".format(len(value), key.upper()))
    for item in value:
      print(item)
    print()

def print_info(coding):
    # for key, value in coding.items():
    #     print(key, value)
    for key in coding:
        print(key, len(coding[key]))
        for value in coding[key]:
            print(value)
        print()
        # print(coding[key])

    # print(dojo["locations"])
    # print(dojo["instructors"])
    # print(dojo["instructors"][0])

printInfo(dojo)
print_info(dojo)
# # output:
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
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print("* * * * "*4)
def printAgain(dicta):
  # print(dicta)
  # for key, value in dicta.items():
  #   print(key, value)
  
  for key in dicta:
    print(key.upper(), len(dicta[key]))
    for val in dicta[key]:
      # print('--- key->', key, 'val->', val)
      print(val)
    print()
printAgain(dojo)