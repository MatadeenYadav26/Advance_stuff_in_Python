#lambdda expression / Functions:

# square = lambda a:print(a**2)

# square(12)

# add = lambda x,y : x+y

# print(add(2,4))

#Mapping:

# a = [1,2,3,4,5]
#Method-1:
# l = []
# for i in a :
#     l.append(i**2)

# print(l)

# #Method-2 : Mapping
# l = map(lambda x:x**2,a)
# print(list((l)))

#Filter:

# l = filter(lambda x : x%2==0,a)

# print(list(l))

# zip:

# name = ["aman" , "rahul" , "Virat"]
# age = [21,29,37]

# comb = zip(name,age)
# # print(list(comb))
# print(dict(list(comb)))

#List Comprehension ,Set Comprehension,  Dictionary Comprehension. 

# a = [1,2,3,4,5,6,7,8,9]

# l= [i for i in a if i%2 ==0]
# s= {i for i in a if i%2 ==0}
# d= {i:i**2 for i in a if i%2 ==0}


# print(l)
# print(s)
# print(d)

#Generators:
# def my_generator():
#     for i in range(5):
#         yield(i)

# gen = my_generator()

# print(next(gen))
# print(next(gen))
# print(list(gen))

#compression in Generators:

# sequence  = (x**2 for x in range(5))

# print(next(sequence))
# print(next(sequence))
# print(next(sequence))

#Decorators:

# def my_decorator(func):
#     def wrapper():
#             print("Hello , i will print before.")
#             func()
#             print("Hello , i will print after.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("hello")

# say_hello()

def decorate(func):
    def wrapper (a,b):
        print("Your 2 number addition is: ")
        func(a,b)
        print('Thankyou')
    return wrapper

@decorate
def add(a,b):
    print(a+b)

add(12,12)