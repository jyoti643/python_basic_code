# total=0
# for i in range(2,21,2):
#     print(i)
#     total+=i
# print("Addition : ",total)
# for i in range(6):
#     print("*"*i)
# for i in range(5,0,-1):
#     print("*"*i)
# a=int(input("Enter the number: "))
# for i in range(1,11):
#     print(a,"x",i,i*a)
# a=int(input("Enter the number: "))
# for i in range(2,11):
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)
#     print()

#print pyramid pattern
# for i in range(1,6):
#     for j in range(1,5-i+1):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()

#simple if else 

#make calculator
a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
op=str(input("Enter the opt: "))

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="/":
    print(a/b)
elif op=="*":
    print(a*b)
