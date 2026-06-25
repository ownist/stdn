# =======================
# ১ থেকে ৫০ পর্যন্ত সব জোড় সংখ্যাগুলোর যোগফল বের করো একটি লুপ ব্যবহার করে।
# =======================
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


print("\n")


# ==============================
# ইউজার থেকে একটি অক্ষর (Character) ইনপুট নাও এবং সেটি ভাওয়েল নাকি কনসোনেন্ট তা if-else দিয়ে চেক করো।
# ==============================
def chek_vowel(char):
    char_lower = char.lower()

    if (
        char_lower == "a"
        or char_lower == "e"
        or char_lower == "i"
        or char_lower == "o"
        or char_lower == "u"
    ):
        return f"{char} is a vowel"

    return f"{char} is not a vowel, {char} is a conconent"


print(chek_vowel("o"))


print("\n")


# ===========================
# একটি লিস্ট থেকে সবচেয়ে ছোট সংখ্যাটি খুঁজে বের করার ফাংশন লেখো। (যেমন: [5, 2, 9, 1, 6] থেকে 1 বের করবে)।
# ===========================
def find_smallest_number(list):
    smallest_number = list[0]

    for num in list:
        if num < smallest_number:
            smallest_number = num

    return smallest_number


print(find_smallest_number([5, 2, 9, 1, 6]))


print("\n")


# ======================
# ইউজার একটি সংখ্যা ইনপুট দিবে (যেমন: ৫), আর তোমার প্রোগ্রাম ওই সংখ্যার নামতা (Multiplication Table) ১০ পর্যন্ত প্রিন্ট করবে।
# ======================
def multiplicatoin_table():
    number = int(input("Enter the number: "))

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


multiplicatoin_table()


print("\n")


# =========================
# একটি লিস্ট দেওয়া আছে [10, 20, 30, 40, 50]। কোনো বিল্ট-ইন ফাংশন ছাড়া লুপ ব্যবহার করে এই লিস্টটিকে উল্টো করে আরেকটি নতুন লিস্টে রাখো।
# =========================
def reverse_list(list):
    rev_list = []

    for num in list:
        rev_list.insert(0, num)

    return rev_list


print(reverse_list([10, 20, 30, 40, 50]))

# using append method
original_list = [1, 2, 3, 4, 5]
rev = []

for i in range(len(original_list) - 1, -1, -1):
    rev.append(original_list[i])

print(rev)


print("\n")


# ==================================
# একটি ভ্যারিয়েবলে একটি সংখ্যা সেভ করো (ধরো secret_number = 7)। এবার ইউজারকে ইনপুট দিতে বলো। ইউজার সঠিক সংখ্যা না বলা পর্যন্ত while লুপের মাধ্যমে ইনপুট নিতেই থাকো। মিলে গেলে বলো "Congratulations!"।
# ==================================
def number_guessing():
    secret_num = 4

    while True:
        user_num = int(input("Enter the correct number: "))

        if user_num == secret_num:
            print(f"Congo! {user_num} is the correct secret number")
            break


number_guessing()
