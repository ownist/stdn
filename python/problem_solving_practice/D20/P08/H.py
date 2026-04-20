user_password = input("Enter your password: ")

if user_password == "admin123":
    print("Access Granted: apni probesh korte perechen!")
elif len(user_password) == 0:
    print("Error: password khali rakha jabe nh.")
else:
    print("Access Denied: vul password, abar chesta korun")
