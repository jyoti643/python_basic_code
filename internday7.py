#lamda function
# a=lambda a,b:print(a+b)
# a(5,7)

# even_no=[]
# for i in range(0,50,2):
#     even_no.append(i)
# print(even_no)

# a=print(list(range(0,50,4)))
# print(a)

# a=lambda: print(list(range(0,5000,1090)))
# a()

# a=lambda a,b,op:print(a+b) if op=="add" else print(a-b) if op=="sub" else print(a*b) if op=="mul" else print(a/b) if op =="div" else print("Invalid operation")
# a(45,5,"add")
# a(56,6,"sub")

# list1=[1,2,3,4,5]
# list2=list(map(lambda x:x*x,list1))
# print(list2)

# products=[{"name":"product A","price":45},{"name":"product b","price":65},{"name":"product c","price":60},{"name":"product d","price":95}]
# filtered_products=list(filter(lambda product:product["price"] > 50,products))
# print(filtered_products)


#Calculating Grades:
# scores=[92,45,35,60,85]
# get_grade=lambda score:"A" if score>=90 else "B" if score>=80 else "C" if score>=70 else "D"
# grade=list(map(get_grade,scores))
# print(grade)

#sorting a list of strings by length:
# 

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# def ordinary():
#     print("I am ordinary")
# decorated_func=make_pretty(ordinary)
# decorated_func()

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
     print("I am ordinary")
ordinary()


def make_sus(func):
    def inner():
        print("you are suspious")
        func()
    return inner
@make_pretty
def ordinary():
     print("I am ordinary")
ordinary()
