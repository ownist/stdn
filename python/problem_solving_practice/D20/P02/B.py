num = int(input("Enter your mark: "))  # mark store

# edge case: valid number check
if num < 0 or num > 100:
    print(f"{num} vul input! number obossoi 0 theke 100 er moddhe hote hbe")
    exit()
elif num >= 90:
    print("Grade A")
elif num >= 80:
    print("Grade B")
elif num >= 70:
    print("Grade C")
elif num >= 60:
    print("Grade D")
else:
    print("Fail")
