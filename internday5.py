import random
print(random.randint(0000,9999))#used to generate number from 0000 to 9999
print(random.random())#generate a random number from 0 to 1
print(random.uniform(10,20))#used to generate a float value between 10 to 20
a=["head","tail"]
print(random.choice(a))

a=["apple","banana","cherry","berry"]
print(random.sample(a,2))
random.shuffle(a)
print(a)

