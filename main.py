# li = [9,1,8,2,7,3,6,4,5]
#
# s_li = sorted(li, reverse=True) # sorting as a new list
#
# print('Sorted Variable:\t', s_li)
#
# li.sort()
#
# print('Orginal Variable:\t', li)

tup = (9,1,8,2,7,3,6,4,5)

s_tup = sorted(tup)

print('Tuple\t', s_tup)

di = {'name': 'Test', 'job': 'programming', 'age': None, 'os': 'Windows'}

s_di = sorted(di)

print('Dict\t', s_di)

li = [-6,-5,-4,1,2,3]

s_li = sorted(li, key=abs)

print (s_li)
