# and ,or ,not

high_income = False


good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eligible")
elif high_income or good_credit or not student:
    print("maybe")
else:
    print("not")
