"""
Extracting information from web pages

Available wepages:
https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/mother.html
https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html
https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html
"""
from urllib.request import urlopen


# Opening web pages
url = 'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/mother.html'  # noqa
page = urlopen(url)
print('\n\n\npage:', page)

# Reading and Decoding
web_page = page.read().decode('utf-8')
print('\n\n\nType of the read data:', type(web_page))
print(f"""\n\n
First 100 chars of the read data:\n
---------------------------------------------------------
{web_page[:100]}
---------------------------------------------------------
""")

# Finding the title in the page
start = web_page.find('<title')
finish = web_page.find('</title>') + len('</title>')
print('\n\n\nTitle tag in web page:\n', web_page[start:finish])

# Counting div and img tags
print(f"""\n\n\n
How many div tags are?: {web_page.count('<div')}
How many img tags are?: {web_page.count('<img')}
""")
