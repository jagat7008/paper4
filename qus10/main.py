from functools import reduce
l1=['a','b']
l2=[1,2]
my_dict=dict(zip(l1,l2))
total_sum=reduce(lambda x,y: x+y, my_dict.values())
print(my_dict)
print(total_sum)