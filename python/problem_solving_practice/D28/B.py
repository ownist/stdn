# ২. তাপমাত্রা রূপান্তর: সেলসিয়াস থেকে ফারেনহাইটে তাপমাত্রা রূপান্তর করার একটি প্রোগ্রাম লিখুন। সূত্র: F = (C * 9/5) + 32।


def convert_cel_to_fahren(cel):
    f = (cel * 9 / 5) + 32
    print(int(f))


convert_cel_to_fahren(20)
