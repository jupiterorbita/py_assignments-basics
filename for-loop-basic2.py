# # Assignment: For Loop Basic II

# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(lista):
  # print(lista)
  for n in range(len(lista)):
    if lista[n] > 0:
      # print(lista[n])
      lista[n] = "big"
  print(lista)
  return lista
# biggie_size([-1, 3, 5, -5]) # returns that same list, but whose values are now [-1, "big", "big", -5]



# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(lista):
  count = 0;
  for n in range(len(lista)):
    if lista[n] > 0:
      count += 1
  lista[len(lista)-1] = count
  print(lista)
  return lista
# count_positives([-1,1,1,1]) # changes the original list to [-1,1,1,3] and returns it
# count_positives([1,6,-4,-2,-7,-2]) # changes the list to [1,6,-4,-2,-7,2] and returns it



# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(lista):
  sum = 0
  for n in lista:
    sum += n
  print(sum)
  return sum
# sum_total([1,2,3,4]) # should return 10
# sum_total([6,3,-2]) # should return 7


# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(list):
  sum = 0
  for n in list:
    sum += n
  return sum / len(list)
# x = average([1,2,3,4]) # should return 2.5
# print(x)


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(list):
  return len(list)
# length([37,2,1,-9]) # should return 4
# length([]) # should return 0

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(list):
  if list == []: return False
  min = list[0]
  for n in range(len(list)):
    if list[n] < min:
      min = list[n]
  print(min)
  return min
# minimum([37,2,1,-9]) # should return -9
# minimum([]) # should return False

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(list):
  if len(list) == 0: return False
  # if len(list) < 1: return False
  # if list == []: return False
  max = list[0]
  for n in range(len(list)):
    if list[n] > max:
      max = list[n]
  print(max)
  return max
maximum([37,2,1,-9]) # should return 37
# print(maximum([])) # should return False

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(list):
  sumTotal = 0
  average = 0
  min = list[0]
  max = list[0]
  for n in range(len(list)):
    # max
    if list[n] > max:
      max = list[n]
    if list[n] < min:
      min = list[n]
    sumTotal += list[n]
  average = sumTotal / len(list)
  return {'sumTotal': sumTotal, 'average': average, 'minimum': min, 'maximum': max, 'length': len(list) }
# print(ultimate_analysis([37,2,1,-9])) 
# should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(list):
  for n in range(int(len(list)/2)):
    temp = list[n]
    list[n] = list[len(list)-1-n]
    list[len(list)-1-n] = temp
  print(list)
# reverse_list([37,2,1,-9]) # should return [-9,1,2,37]

