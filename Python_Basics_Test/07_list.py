l1 = [10,30,11,50,"a","z","jg",(8,16,24),{1:100, 2:200}]

l2 = [1,5,4,3,1,1,6,7,8]

# print(l2+l1)


print(l2.sort(reverse=False))
print(l2)
l3= [45,32,1,33,87,65,445,65]
# print(l3[10])     --->
#  IndexError: list index out of range
l2.extend(l3)
print(l2)