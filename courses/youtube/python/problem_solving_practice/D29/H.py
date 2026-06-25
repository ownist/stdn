# ফাঁকা স্ট্রিং: ইউজার ইনপুট দেওয়ার সময় কিছু না লিখে এন্টার দিলে তাকে একটি সতর্কবার্তা দিন।
data = input("enter your name: ")

if len(data) == 0:
    print("plz enter your name")
else:
    print(f"hey {data}! how is it going?")
