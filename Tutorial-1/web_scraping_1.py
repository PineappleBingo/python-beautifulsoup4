import os
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = "\\".join([ROOT_DIR, "index.html"])

# Open html doc as bs4 object
with open(file_path, "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print html doc with foramtting
print(doc.prettify)

# access element by tag name
tag = doc.title
print(tag.string)
tag.string = "New Title"
print(tag)

# find all tags find_all()
tags = doc.find_all("a")
print(tags)

# access first tag
print("len:", len(tags))
tags = doc.find_all("a")[0]
print(tags)

# print strings in each tag
for tag in tags:
    print(tag.string)

# access the nested tag
tags = doc.find_all("a")[4]
print(tags.find_all("b"))