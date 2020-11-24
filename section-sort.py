arr = [9,57,8,2,55,3]
print('\n\noriginal arr -> ', arr)

def sectionSort(arr):
  min = arr[0]
  for j in range(len(arr)-1):
    print('--'*20, 'Iternation j=',j)
    print('arr is ', arr)
    for i in range(j,len(arr)-1):
      print('\n', '*'*30, 'i=',i, 'arr[i]=', arr[i])
      print('[i] loop arr is ->', arr)
      print(f'comparing min={min}, with arr[{i}]->, {arr[i]}')
      if arr[i] < min:
        print('swapping', min, 'with', arr[i])
        # set new min
        min = arr[i]
        # whatever min was make it the first item in the arr and continue loop
      # else:
      #   print('no --- swap')
      if arr[0+j] == min:
        print('IF arr[0+j] is already the same as min', arr[0+j], min)
        # break
      elif arr[0+j] > min:
        arr[0+j] = min
        arr[i] = arr[0+j]
        # break
      # after we find min swap
      print('at the end of the i loop i=', i, 'j=', j)
      print('???what is arr[0+j], arr[',0+j,'] ->', arr[0+j])
      
      # change arr[i] with start *** * ** * * * *
      
    print('* * * min is now ->', min)
  print('arr is now ->', arr)
      # break
sectionSort(arr)