# লিপ ইয়ার: একটি বছর ইনপুট নিন এবং সেটি লিপ ইয়ার (Leap Year) কি না তা যাচাই করুন।

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
