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


print("\n")


# ===========================
# একটি লিস্টে কিছু নাম আছে। ইউজার একটি নাম ইনপুট দিলে লুপ চালিয়ে চেক করো ওই নামটি লিস্টে আছে কি না। থাকলে বলো "Found", না থাকলে "Not Found"।
# ===========================
def checkList(list, user_input):
    for item in list:
        if item == user_input:
            return f"{user_input} is found in {list}"

    return f"{user_input} is not found in {list}"


print(checkList([12, 54, 26, 84, 65], 65))
