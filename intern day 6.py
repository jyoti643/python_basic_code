#day 6 code 1
# def greet(name,msg="hello"):
#     print(f"{msg},{name}")

# greet("Ri","hey")#or option greet(name="Ri",msg="hey") but does not work in the case of multiple arguments
# greet("Siya")
# greet("geet")

#day 6 code 1
# def greet(name,msg="hello"):
#     return f"{msg},{name}"

# print(greet("Ri","hey"))#or option greet(name="Ri",msg="hey") but does not work in the case of multiple arguments
# print(greet("Siya"))
# print(greet("geet"))

#early exit
# def divide_numbers(x,y):
#     if y==0:   
#         return "Cannot divide by zero"
#     result = x / y
#     return result

# print(divide_numbers(36,6))

#program to find sum of multiple numbers using arbitary arguments
# def find_sum(*numbers):
#     result=0
#     for num in numbers:
#         result= result + num
#         print("Sum = ",result)
# print(find_sum(1,56,112,2432,48793))

# def choice():
#     while True:
#         print("welcome to online calculator.\n enter 1 for addtion\nEnter 2 for subtraction \nEnter 3 for multiplication\nEnter 4 for division\n enter 5 for the exit .\n.......................................   ")
#         ch=int(input("Please enter the choice for desired operation (1 to 5) : "))
#         if ch in range(1,5):
#             a=int(input("Enter the first number : "))
#             b=int(input("Enter the second number : "))
#             if ch==1:
#                 print(add(a,b))
#             elif ch==2:
#                 print(sub(a,b))
#             elif ch==3:
#                 print(mul(a,b))
#             elif ch==4:
#                 print(div(a,b))
#         elif ch==5:
#                 print("bye,will meet again when you need me.......")
#                 continue
        
#         else:
#             print("Please enter a valid choice")

# def add(n1,n2):
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     if n2==0:
#         return "cannot divide by zero"
#     else:
#         return n1/n2
# choice()

#recurssive function
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print("factorial : ",factorial(5))


