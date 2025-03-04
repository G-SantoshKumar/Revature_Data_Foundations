#text_file=open("sample.txt")
#print(type(text_file))
#print(text_file.read())
#text_file.close()

with open("sample.txt",'r') as file:
    content=file.read()
print(content)

#with open("sample.txt",'a+') as file:
 #   content=file.write("\nHIi")

with open("sample.txt",'r') as source_file, open("file1.py","w") as dest_file:
    content = source_file.read()  
    dest_file.write(content) 
