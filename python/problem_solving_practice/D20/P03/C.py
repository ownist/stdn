num = int(input("Enter your range: "))
total_sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)
        total_sum += i


# print total sum
print(f"total sum of even numbers: {total_sum}")


# ----------------------- AI suggession, pythonic way -----------------------
for i in range(2, num + 1, 2):
    print(i)
