# class A():
#     def __init__(self):
#         self.income=50000
#         self.earning=60000
# class B(A):
#     def total(self):
#         self.amount=self.income  +self.earning
#         print(self.amount)
# obj=B()
# obj.total()


# class A():
#     def sum(self):
#         self.income=50000
#         self.earning=60000
# class B(A):
#     def total(self):
#         self.amount=self.income  +self.earning
#         print(self.amount)
# obj=B()
# obj.sum()
# obj.total()


# class A():
#     def ab(self):
#         print("welcome to the heaven")
# class B(A):
#     def bc(self):
#         print("welcome to the hell")
# class C(B):
#     def cd(self):
#         print("welcome to the earth due to the neutral karma")
# o=C()
# b=B()
# o.ab()
# b.bc()
# o.cd()


# class A():
#     def ab(self):
#         print("welcome to the neptune")
# class B(A):
#     def bc(self):
#         print("welcome to planet pluto")
# class C():
#     def cd(self):
#         print("human you will be destroyed if you will  come near them!!!!\n-  JUPITOR")
# class D(B,C):
#     def de(self):
#         print("do not try,beware aware or be lost in this universe\n" \
#         "if you are not afraid so try,but you are warned ")
# o=D()
# o.ab()
# o.bc()
# o.cd()
# o.de()

# class MathOperations:
#     def add(self,a,b=0,c=0):
#         return a+b+c
# math_obj=MathOperations()
# #using the add method in different ways
# result1=math_obj.add(5)
# result2=math_obj.add(5,3)
# result3=math_obj.add(5,3,2)
# print(result1,result2,result3)
    

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("dog barks")

# d=Dog()
# d.sound()

# class SalesSection:
#     def _init_(self):
#         # Assume sales data is stored in a private attribute
#         self._sales_data = {}

#     def add_sale(self, month, amount):
#         # Method to add sales data
#         self._sales_data[month] = amount

#     def get_sales_data(self, month):
#         # Method to retrieve sales data for a specific month
#         return self._sales_data.get(month, "No data available for the specified month")


# class FinanceSection:
#     def _init_(self):
#         # Assume financial data is stored in a private attribute
#         self._financial_data = {}

#     def add_transaction(self, month, transaction_amount):
#         # Method to add financial transaction data
#         self._financial_data[month] = transaction_amount

#     def get_financial_data(self, month):
#         # Method to retrieve financial data for a specific month
#         return self._financial_data.get(month, "No data available for the specified month")


# sales_section = SalesSection()
# finance_section = FinanceSection()

# # Adding sales data
# sales_section.add_sale("January", 50000)
# sales_section.add_sale("February", 60000)
# sales_section.add_sale("March", 75000)

# # Adding financial transaction data
# finance_section.add_transaction("January", 20000)
# finance_section.add_transaction("February", 25000)
# finance_section.add_transaction("March", 30000)

# # An official from the finance section wants sales data for January
# requested_month = "February"
# sales_data_for_requested_month = sales_section.get_sales_data(requested_month)
# print(f"Sales data for {requested_month}: {sales_data_for_requested_month}")

# # An official from the finance section wants financial data for January
# financial_data_for_requested_month = finance_section.get_financial_data(requested_month)
# print(f"Financial data for {requested_month}: {financial_data_for_requested_month}")


#Abstract class
# class Payment(ABC):
#     @abstractmethod
#     def make_payment(delf,amount):
#         pass

# class creditcardpayment(Payment)
    