from bs4 import BeautifulSoup 
import requests

page = requests.get("https://www.pythonscraping.com/pages/page1.html")
soup = BeautifulSoup(page.text, "html.parser")

with open(".txt", 'w') as file:
	file.write(soup.find("div").text)
