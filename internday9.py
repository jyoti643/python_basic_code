# class add():
#     a=20
#     b=30
#     def sub(self):
#         self.c=self.a-self.b
#         print(self.c)

# obj = add()
# obj.sub()

# class add():
#     a=20
#     b=30
#     def _init_(self): #contuctor
#         self.c=self.b*self.a
#         print(self.c)
# obj=add()

# class average():
#     a=int(input("Enter marks of subject1 : "))
#     b=int(input("Enter marks of subject2 : "))
#     c=int(input("Enter marks of subject3 : "))
#     def avg(self):
#         self.avge = (self.a+self.b+self.c)//3
#         print("average of three subjects is",self.avge)
# o=average()
# o.avg()

# class per():
#     a=int(input("Enter marks of subject1 : "))
#     b=int(input("Enter marks of subject2 : "))
#     c=int(input("Enter marks of subject3 :"))
#     def avg(self):
#         self.avge = (self.a+self.b+self.c)//3
#         print(f"% of three subjects is",self.avge)
# o=per()
# o.avg()

# class parent():
#     def add(self):
#         self.a=40
#         self.b=30
#         self.c = self.a + self.b
#         print(self.c)
# class child (parent):
#     def sub (self):
#         self.d=20
#         self.e=50
#         self.w = self.d - self.e
#         print(self.w)
# obj = child()
# obj.add()
# obj.sub()


# class A():
#     a=int(input("Enter the number1 : "))
#     b=int(input("Enter the number2 : "))
#     def add(self):
#         self.c = self.a + self.b
#         print(self.c)
# class B(A):
#     def sub(self):
#         self.c = self.a - self.b
#         print(self.c)
# class C(B):
#     def mul(self):
#         self.c = self.a * self.b
#         print(self.c)
# class D(C):
#     def div(self):
#         self.c = self.a / self.b
#         print(self.c)
# obj=D()
# obj.add()
# obj.sub()
# obj.mul()
# obj.div()

#multiple inheritance
# class A():
#     def a(self):
#         print("hi")
# class B():
#     def b(self):
#         print("python")

# class C(A,B):
#     def c(self):
#         print("!")

# obj = C()
# obj.a()
# obj.b()
# obj.c()

