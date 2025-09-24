def greet(first_name,last_name):
    print(f"hi bro {first_name} {last_name}")
    print("welcome here")


greet("binay","kurmi")

#types of function
# 1- perform a task
# 2- return a value

def get_greeting(name):
    return f"hi {name}"

message = get_greeting("binay")
print(message)

file =open("content.txt","w")
file.write(message)