"""
تمرین دوم
برنامه ای بنویس که یک متن از ورودی دریافت کند و همانند مثال زیر، از اول تا اولین نقطه آن متن را چاپ کند.
Enter: my name is amirhossein. i live in tehran.
my name is amirhossein
"""

text = input("Enter: ")
print(text.split(".")[0])
print(text[:text.find(".")])