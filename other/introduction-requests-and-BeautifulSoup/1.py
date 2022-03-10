from bs4 import BeautifulSoup 
import requests

page = requests.get("https://www.python.org/")
soup = BeautifulSoup(page.text, "html.parser")

print(soup)
