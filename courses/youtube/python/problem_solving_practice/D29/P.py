# সহজ চ্যাটবট: একটি ফাংশন লিখুন যা "কেমন আছো?" বললে উত্তর দেবে "ভালো আছি", আর "তোমার নাম কি?" বললে নিজের নাম বলবে।
def chatbot():
    user_input = input("what is your mind: ")

    if user_input == "kmn acho":
        print("valo achi")
    elif user_input == "tmr name ki":
        print("amr name ownist")


chatbot()
