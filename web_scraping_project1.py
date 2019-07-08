import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

all_quotes=[]
base_url="http://quotes.toscrape.com"
url="/page/1"

while url:
	res=requests.get(f"{base_url}{url}")
	#print(f"Now Scraping {base_url}{url}.....")
	soup=BeautifulSoup(res.text,"html.parser")
	quotes=soup.find_all(class_="quote")
	for quote in quotes:
		all_quotes.append({
			"QUOTE":quote.find(class_="text").get_text(),
			"AUTHOR":quote.find(class_="author").get_text(),
			"URL":quote.find("a")["href"]
			})

	next_page=soup.find(class_="next")
	if next_page:
		url=next_page.find("a")["href"]
	else:
		url=None
	#sleep(2)	

with open("web_scraping_project.csv","w",newline='') as csv_file:
	headers=["QUOTE","AUTHOR","URL"]
	csv_writer=DictWriter(csv_file,fieldnames=headers)
	csv_writer.writeheader()
	for quote in all_quotes:
		csv_writer.writerow(quote)
