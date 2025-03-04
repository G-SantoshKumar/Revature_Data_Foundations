text = "Hello World!"

res=tuple(set(char.lower() for char in text if char.isalpha()))

print(res)