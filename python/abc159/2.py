text = input()
index = (len(text)-1)//2

# print(text[:index])
# print(print(text[:index][::-1]))

# print(text[index+1:])

if text[::-1] == text and text[:index][::-1] == text[:index] and text[index+1:][::-1] == text[index+1:]:
    print("Yes")
else:
    print("No")