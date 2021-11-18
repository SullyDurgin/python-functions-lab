num_li = []
num = int(input('How many numbers in list: '))

for i in range(num):
  nums = int(input('Enter number '))
  num_li.append(nums)

  print('The largest number in the list is :', max(num_li))