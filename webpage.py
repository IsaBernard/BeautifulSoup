from bs4 import BeautifulSoup

# To keep things simple and also reproducible, consider the following HTML code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

# write in a index.html file (can be opened in browser)
with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, 'lxml')

# format the html code:
# print(soup.prettify())

# Tag:
# from the top of the page will find the first occurrence of a "b"
# print(soup.b)

# similar, but for all "b" tags
# print(soup.find_all('b'))

# Name: fives the name of the tag, here 'b'
# print(soup.b.name)

# # To alter the name of the tag:
# tag = soup.b
# print(tag)
# tag.name = "blockquote"
# print(tag)

# # Attributes: here, give me the 3rd element from the list of all 'b' tag extracted
# tag = soup.find_all('b')[2]
# print(tag)
# # >>> <b id="1">Test 1</b>
# # This is a bold tag, but it has an attribute id (here =1)
# print(tag['id'])

tag = soup.find_all('b')[3]
# now, two attributes
# print(tag)
# print(tag['id'])
# print(tag['another-attribute'])
#
# # to see all attributes without knowing
# print(tag.attrs)

# # These properties are mutable, and we can alter them
# # in the following manner.
# print(tag)
# tag['another-attribute'] = 2
# print(tag)

# # We can also use Python's del command for lists to
# # remove attributes:
# del tag['id']
# del tag['another-attribute']
# print(tag)

# Print the content between the (here multi-valued) attributes
tag = soup.find_all('b')[3]
print(tag)
print(tag.string)

# We can use the "replace_with" function to replace the content for something else
tag.string.replace_with("This is another string")
print(tag)
print(tag.string)
