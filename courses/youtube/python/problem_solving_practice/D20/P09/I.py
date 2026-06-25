age = int(input("Enter your age: "))

if age < 5:
    print("apner ticket free.")
elif age >= 5 and age <= 12:
    print("ticket er dam 5 tk.")
elif age >= 13 and age <= 59:
    print("ticket er dam 10 tk.")
else:
    print("ticket er dam 7 tk (senior citizen discount)")
