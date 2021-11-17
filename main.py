from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import os

# Create a new chat bot named Jarvis
bot= ChatBot('Jarvis')

# Start the trainer
trainer = ListTrainer(bot)

# Path for training data
for file in os.listdir('C:/Users/Anonymous/Desktop/ChatBot/files/data/'):

    chats = open('C:/Users/Anonymous/Desktop/ChatBot/files/data/' + file, 'r').readlines()

    trainer.train(chats)

# Initialize Conversation
name=input( "Jarvis : Hii, my name is Jarvis. How can I call you? \n-> ")

print('Hi',name,'nice to meet you')

while True:

    request = input (name + ":- ")

    # Get a response to the input request
    response = bot.get_response(request)

    # Print response if confidence greater than 0.1
    if response.confidence > 0.1:
        
        print('Jarvis : ', response, '\n')
 
    # If request is bye terminate the bot
    elif request == ("bye"):

        print('Hope to see you soon '+ name)

        break
    
    # If request not found in data scrape results from wikipedia
    else:
        
        try:
            url  = "https://en.wikipedia.org/wiki/"+ request
            page = get(url).text
            soup = BeautifulSoup(page,"lxml")
            p    = soup.find_all("p")
            print(p[1].text)

        except Exception as error:
            
            print('Jarvis: Sorry i have no idea about that.')