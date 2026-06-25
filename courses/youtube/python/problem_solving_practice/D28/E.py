# নামতা: যেকোনো একটি সংখ্যার নামতা (১ থেকে ১০ পর্যন্ত) প্রিন্ট করুন।

n = int(input("Enter namoter numer: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
