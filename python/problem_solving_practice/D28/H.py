# বড় সংখ্যা নির্ণয়: তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যাটি খুঁজে বের করার জন্য একটি ফাংশন তৈরি করুন।

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
