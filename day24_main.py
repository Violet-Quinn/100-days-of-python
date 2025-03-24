# file=open("my_file.txt")
# content=file.read()
# print(content)
# file.close()

with open("my_file.txt") as f:
    content=f.read()
    print(content)

# with open("my_file.txt",mode="w") as file:
#     file.write("writing into file")
