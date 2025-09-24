# def greet(name):
#     print(f"hi{name}")
    
# print(greet("binay"))  #in python all functions returns none by default

#keyword arguments
def increment(num,by):
    return num+by

print(increment(num=4,by=5))


#default arguments
def increment(num,by=2):
    return num+by

print(increment(num=4))
print(increment(num=4,by=3))


