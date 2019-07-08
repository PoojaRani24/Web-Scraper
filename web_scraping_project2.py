import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictReader

all_quotes=[]
base_url="http://quotes.toscrape.com"
url="/page/1"

with open("web_scraping_project.csv") as csv_file:
	csv_reader=DictReader(csv_file)
	for quote in csv_reader:
		all_quotes.append(quote)
		#print(all_quotes)

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
			#sleep(1)
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
	while user_choice.lower() not in ["yes","y","n","no"]:
		user_choice=input("Would youlike to play again?(y/n)\n")

	if user_choice.lower()=="y" or user_choice.lower()=="yes":
	 	game=1
	else:
		print("OK,GOODBYE!!")
		game=0
