print("hello world")
2+2
x = 6
y = 9
course = "Python \"progg"
print(len(course))
print(course[0:4])
print(course[0:])
print(course[-1])
print(course[:4])
print(course[:])

# this is a comment
# escape characters : \' ,\"  ,\\  ,\n

first = "binay"
second = "kurmi"
# full = first + second
full =f" {first} {second}"



print(full)

print(course.upper())
print(course.lower())
print(course.title())
print(course.strip()) #remove space from both left and right side
print(course.lstrip()) #remove space from left 
print(course.rstrip()) #remove space from right

print(course.find("ro"))  # \ is ignored
print(course.replace("p","j"))
print("Py" in course)
