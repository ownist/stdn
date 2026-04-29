# ভোটের যোগ্যতা: ইউজার কি বাংলাদেশের নাগরিক এবং তার বয়স কি ১৮-এর বেশি? এই দুটি তথ্য যাচাই করে সে ভোট দিতে পারবে কি না তা জানান।
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18 and nationality.lower() == "bangladeshi":
    print("you can vote")
else:
    print("you cannot vote")
