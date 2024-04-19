"""
Extracting information from web pages

Available wepages:
https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/mother.html
https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html
https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen


print('\n\n\nPython pkg:', BeautifulSoup)

# Reading the page
url = 'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html'  # noqa
page = urlopen(url)
html = page.read().decode('utf-8')

# Reading HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print('\n\n\nType of the read html with BeautifulSoup:', type(soup))
print(f"""\n\n
HTML read:\n
---------------------------------------------------------
{soup()}
---------------------------------------------------------
""")

print(f"""\n\n
HTML read in more pretty format:\n
---------------------------------------------------------
{soup.prettify()}
---------------------------------------------------------
""")

# Finding elements inside
print(f"""\n\n
Printing just the head:\n
---------------------------------------------------------
{soup.head.prettify()}
---------------------------------------------------------
""")

# It is possible to iterate each element inside
print('\n\n\nChildren in head:')
for child in soup.head.children:
    print(child)

# Find the first h1 tag
print('\n\n\nFirst h1 tag:\n', soup.h1)

# Printing all childs belonging to ul tag
print('\n\n\nFound childs in ul')
for child in soup.ul.children:
    print(child)

# Printing the first div
print(f"""\n\n\n
First div tag: {soup.div}
Its attributes: {soup.div.attrs}
Its content: {soup.div.contents}
Only the text: {soup.div.get_text()}
""")

# Using .find() property
print(f"""\n\n\n
First div tag using find property: {soup.find('div')}
Its attributes: {soup.find('div').attrs}
Its content: {soup.find('div').contents}
Only the text: {soup.find('div').get_text()}
""")

# Retrieving all p instances
print('\n\n\n<p> tags:', soup.find_all('p'), sep='\n')

# Finding all <div> and <title> at the same time
print('\n\n\nFinding all <div> and <title>:')
print(soup.find_all(['div', 'title']))

# Counting p elements
print('\n\n\nHow many <p> tags are?', len(soup.find_all('p')))

# Getting all attributes of the div elements
print('\n\n\nAttributes found in each div instance:')
for div in soup.find_all('div'):
    print(div.attrs)

# Getting only the text of the p instances
print('\n\n\nGetting only the text of p instances:')
for p in soup.find_all('p'):
    print(p.get_text())

# Getting all the href attributes of all link instances
print('\n\n\nhref attribute of the found <link>:')
for link in soup.find_all('link'):
    print(link.attrs.get('href'))

# Finding all div with class='box'
print('\n\n\nFinding box div:')
for div in soup.find_all('div', {'class': 'box'}):
    print(div)

# Finding div element with an specific id
print('\n\n\nDiv with id="proper"', soup.find('div', {'id': 'proper'}))
# There is no div with proper id
