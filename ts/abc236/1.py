text = list(str(input()))
start, end = map(int, input().split())  # type(A) => <class 'str'>

text[end], text[start] = text[start], text[end]

print("".join(text))