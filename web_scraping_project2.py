import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

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
print("\n")
game=1
while game:
	quote=choice(all_quotes)
	print("*"*192)
	print("*"*192)
	print("Here's a quote:\n")
	print(quote["QUOTE"])
	print("*"*192)
	print("*"*192)
	#print(quote["AUTHOR"])
	name=quote["AUTHOR"].split(" ")
	last=name[-1]
	print("\n")
	print("Who said this quote?")
	print("\n")
	guess=4
	flag=0
	while guess:
		Answer=input("TAKE A GUESS:")
		guess-=1;
		if Answer.lower()==quote["AUTHOR"].lower():
			flag=1
			break
		else:
			print(f"\nIncorrect guess! Remaining guesses left {guess}\n")
			sleep(1)
			if guess==3:
				#make request to 
				res_author=requests.get(f"{base_url}{quote['URL']}")
				soup_author=BeautifulSoup(res_author.text,"html.parser")
				author_born_date=soup_author.find(class_="author-born-date").get_text()
				author_born_location=soup_author.find(class_="author-born-location").get_text()
				print("*"*192)
				print(f"Hers's a HINT:The author was born on {author_born_date} {author_born_location}\n")
				print("*"*192)
			if guess==2:
				print("*"*192)
				print(f"Here's a HINT:Author's first name begins with {quote['AUTHOR'][0]}\n")
				print("*"*192)
			if guess==1:
				print("*"*192)
				print(f"Here's a HINT:Author's Second name begins with {last[0]}\n")
				print("*"*192)
	if flag==0:
	    print("Sorry,You ran out of Guesses!\n")
	    print("*"*192)
	    print(f"Correct Answer is {quote['AUTHOR']} :)\n")
	    print("*"*192)
	else:
		print("*"*192)
		print("\nYou won!\n")
		print("*"*192)
	user_choice=input("\n\nWould youlike to play again?(y/n)\n")
	if user_choice.lower()=="y" or user_choice.lower()=="yes":
	 	game=1
	else:
		print("OK,GOODBYE!!")
		game=0
	
    
	
    

	

	
	












