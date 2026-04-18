# ---------------------------- while loop ----------------------------

n = 1
while n <= 5:
    print(n)
    n += 1

print("\n")

# ---------------------------- for loop ----------------------------
for i in range(1, 6):
    print(i)


print("\n")


for n in range(1, 11):
    if n % 2 == 0:
        print(n)


print("\n")


# ---------------------------- list print using for loop ----------------------------
my_teams = ["shahed", "rashel", "jihad", "tomjid"]

for p in my_teams:
    print(p.capitalize())


print("\n")


# ---------------------------- loop control ----------------------------

# using while loop
count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1


print("\n")


for i in range(1, 7):
    if i == 4:
        break
    print(i)
