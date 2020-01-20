import re

# sentense = input()
sentense = "dreameraser"

# どちらを先に置換するかを意識する
sentense = re.sub(r'eraser', '',sentense)
sentense = re.sub(r'erase', '',sentense)
sentense = re.sub(r'dreamer', '',sentense)
sentense = re.sub(r'dream', '',sentense)


print(sentense)
print(len(sentense))
