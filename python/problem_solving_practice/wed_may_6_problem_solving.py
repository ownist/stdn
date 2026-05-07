# 1
sum = 0

for n in range(1, 51):
    if n % 2 == 0:
        sum += n


print(sum)

print("\n")


# ==========================
# len() ফাংশন ব্যবহার না করে একটি লুপের সাহায্যে কোনো স্ট্রিংয়ে কতগুলো অক্ষর আছে তা গণনা করো।
# ==========================
def string_char_count(str):
    count = 0

    for char in str:
        count += 1

    return count


print(string_char_count("ownist"))
