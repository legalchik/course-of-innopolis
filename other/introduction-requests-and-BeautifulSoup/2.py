from bs4 import BeautifulSoup 
import requests

page = requests.get("https://scrapingclub.com/exercise/list_basic/")
soup = BeautifulSoup(page.text, "html.parser")

for el in soup.findAll('h4', class_="card-title"):
	print(el.text)
