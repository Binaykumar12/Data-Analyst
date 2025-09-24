# for i in range(2,11,2):
#     print(i)
# print("We have 4 even numbers")
count = 0
for i in range(1, 10):
    if (i % 2 == 0):
        print(i)
        count += 1

print(f"We have {count} even numbers")
