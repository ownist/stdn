# উল্টো শব্দ: ইউজারের কাছ থেকে একটি শব্দ ইনপুট নিয়ে সেটি উল্টো করে (যেমন: 'python' হয়ে যাবে 'nohtyp') প্রিন্ট করুন।
str = input("Enter a string: ")
palindrome = ""

for i in str:
    palindrome = i + palindrome


print(palindrome)
