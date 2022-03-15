from bs4 import BeautifulSoup 
import requests

page = requests.get("https://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(page.text, "html.parser")

for el in soup.findAll(class_="red"):
	print(el.text)
	