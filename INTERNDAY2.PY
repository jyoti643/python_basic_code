#data structure list
# a=[]
# a=[1,2,3]
# a=[12,23,3,a]
# a=[1,2,3,["a","b"],"apple"]

# print(a[0])
# print(a[3][0])
# print(a[4][2])

# negative indexing 


#list slicing
# a=["apple","a",1,2,3,24,52]
# print(a[:1])
# print(a[:5])
# print(a[5:])
# print(a[2:6])
# print(a[::2])
# print(a[::-1])

# list methods
# a=[1,2,3,4,5,6,7,8,9,10]
# a[0]=-1
# print(a)
# a.append(12)
# print(a)

# a.insert(2,12)
# print(a)



# add multiple element
# a.extend([11,12,13])
# print(a)

# # add multiple element using slicing

# a[2:2]=['x','y','z']
# print(a)


# concate list
# b=['a','b','c']
# c=a+b
# print(c)

#repeate list
# a=[1,2,3]
# print(a*5)

#remove element
# a=[1,2,'a',3,4,5,6,7,8,9,10]
# a.remove('a') #specify element inside method
# print(a)
# del a[2:5]
# print(a)

# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i%2!=0:
#         del i
#     else:
#         a.append(i)
# print(a)


#pop
# a=[1,2,3,4,5]
# print(a.pop())
# print(a)
# print(a.pop(0))

# clear
# a=[1,2,3,4,5]
# a.clear()
# print(a)

# del a[3]
# print(a)
# del a
# print(a)

#index
# a=[1,2,3,4,5,2,3]
# print(a.index(3))

#sort
# a=[3,2,1,5,4]
# a.sort()
# print(a)

#reverse
# a=[3,2,1,5,4]
# # a.reverse()
# # print(a)
# a.sort(reverse=True)
# print(a)


#using slicing reversing list
'''a=[3,2,1,5,4]
print(a[::-1])
'''
#decending order sorting
# a = [3, 2, 1, 5, 4]
# print(sorted(a, reverse=True)) 

#count
# a=[1,2,3,4,5,1,2,3]
# print(a.count(2))

# a=(1,2,3,(4,5,63))
# a[3][1]="A"
# print(a)



# a="ravina",
# print(type(a))
#tuple with no element
# a=()

#tuple with integer
# b=(1,2,3,4,5)

#tuple with string
# c=('apple','banana','cherry')

#tuple with mixed data type
# d=(1,'apple',2.5,'banana')

#tuple with nested tuple
# e=(1,2,3,(4,5,6))

#tuple with list
# e=(1,2,3,[4,5,6],[1,2,3])
# e[4][1]=-1
# print(e)
# print(e[4][1])




#tuple with one element
# a=("ravina")
# print(type(a))
# g=(1,)
# print(type(g))


#tuple unpacking
# a=("ravina",27,"BE-EXTC")
# name,age,qualification=a
# print(name)
# print(age)
# print(qualification)

#tuple methods
# 1.index()
# b=(1,2,3,4,5)
# print(b.index(2))

 #2. count()
# f=(1,2,3,4,5,1,2,2)
# print(f.count(1))

#delete
# a=(1,2,3)
# del a


#3. len()
# b=(1,2,3,4,5)
# print(len(b))

#4. max()
# b=(1,2,3,4,5)
# print(max(b))

#5. min()
# b=(1,2,3,4,5)
# print(min(b))

#6. sum()
# b=(1,2,3,4,5)
# print(sum(b))

#7. tuple()
# a=[1,2,3,4]
# print(tuple(a))

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# output=[i+j for i, j in zip(list1,list2)]
# print((output))


###############################################################################################
units = int(input("Enter the number of units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
elif units <= 300:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
else:
    bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15

print(f"Total electricity bill: ₹{bill}")
