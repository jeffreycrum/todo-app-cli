files = ["../files/a.txt", "../files/b.txt", "../files/c.txt"]

for file in files:
    f = open(file, "r")
    content = f.read()
    print(content)