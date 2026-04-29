# গোপন পাসওয়ার্ড: ইউজারের কাছে পাসওয়ার্ড চান। যদি পাসওয়ার্ড "Python123" হয়, তবে "Access Granted" বলুন, নয়তো "Access Denied" বলুন।

password = input("Enter your password: ")

if password == "Python123":
    print("Access Granted")
else:
    print("Access Denied")
