## 2. Webpage structure ##

# Write your code here.
response = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
content = response.content
print(content)

## 3. Retrieving elements from a page ##

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With beautifulsoup, we can access branches by simply using tag types as 
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text of the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

title_text = parser.head.title.text
print(title_text)

## 4. Using find all ##

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag
p = body[0].find_all("p")

# Get the text
print(p[0].text)

title_text = parser.find_all('head')[0].find_all('title')[0].text
print(title_text)

## 5. Element ids ##

# Get the page content and setup a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the id attribute to only get elements with a certain id.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

second_paragraph_text = parser.find_all('p', id='second')[0].text
print(second_paragraph_text)

## 6. Element classes ##

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
print(first_inner_paragraph.text)

second_inner_paragraph_text = parser.find_all('p', class_='inner-text')[1].text
first_outer_paragraph_text = parser.find_all('p', class_='outer-text')[0].text
print(second_inner_paragraph_text, first_outer_paragraph_text)

## 8. Using CSS Selectors ##

# Get the website that contains classes and ids
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all the elements with the first-item class
first_items = parser.select(".first-item")

# Print the text of the first paragraph (first element with the first-item class)
print(first_items[0].text)

first_outer_text = parser.select('.outer-text')[0].text
second_text = parser.select('#second')[0].text
print(first_outer_text, second_text)

## 10. Using Nested CSS Selectors ##

# Get the super bowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number of turnovers committed by the Seahawks.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
print(seahawks_turnovers_count)

patriots_total_plays_count = parser.select('#total-plays')[0].select('td')[2].text
seahawks_total_yards_count = parser.select('#total-yards')[0].select('td')[1].text
print(patriots_total_plays_count, seahawks_total_yards_count)