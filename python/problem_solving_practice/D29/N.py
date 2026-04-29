# বন্ধু খোঁজা: একটি ফাংশন তৈরি করুন যা একটি নাম এবং একটি লিস্ট গ্রহণ করবে। নামটা লিস্টে আছে কি না তা জানিয়ে দেবে।


def khuja(name, list):
    for i in list:
        if i == name:
            return "yup goted"


print(khuja("ownist", ["shahed", "sabbir", "ownist"]))
