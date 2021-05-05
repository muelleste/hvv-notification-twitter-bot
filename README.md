# HVV-Notification-Twitter-Bot

## Prolog

This small tool is for searching in the twitter api, to get latest informations about the traffic sitatuion. 
There are a few twitter accounts, who are posting the latest disturbances on twitter. So I created a small twitter bot, who works with a local cache to send telegram messages to inform me. 
Telegram was the message, which has got a free API and I am using this app very often. 

## Requirements
For using this container on your pc, raspberry must be *'docker'* and *'docker-compose'* installed.

### Edit API.py 
In the first lines of this programm, i define a few variables.

```python
busline = 8800
sbahn = "S2"
```
Here I am defining, which are the **key words** in the tweets.
 

```python
telegramId = <TelegramID>
telegramBotId = <TelegramBotID>
consumer_key="<TwitterAPI ConsumerKey>"
consumer_secret="<TwitterAPI ConsumerSecret>"

access_token="<TwitterAPI Access Token>"
access_token_secret="<TwitterAPI Access Token Secret>"
``` 
| variable | advices | 
| ------   | ------- | 
| telegramId | this is my telegram id, this bot is sending directly to me messages. How2Find my Telegram-ID: https://www.alphr.com/telegram-find-user-id/ | 
| telegramBotId | access keys for the telegram bot itself, for sending messages. | 
| consumer_key & consumer_secret | this is the key for access the twitter api. You need your own Consumer Key & Secret: https://developer.twitter.com | 
| access_token & access_token_secret | you will find it in your twitter api account | 

## Installation

- First of all install python3 and python3-pip
> root # apt install python3 python3-pip git
- Clone this Git-Repo
> root # git clone https://github.com/muelleste/hvv-notification-twitter-bot.git
- Change to the directory
> root # cd hvv-notification-twitter-bot
- Edit api.py
> root # vim api.py
- Build Docker Container
> root # docker build . -t hvv
- Start Container with Docker-Compose
> root # docker-compose up -d 

## Configuration 

In *'Main'* there are a few configuration paramters definied. 
```python
	generalSearchTwitterAPI("vhhbus","vhhbus.csv","bus")
        generalSearchTwitterAPI("HVVStoerungen","hvvStoerungen.csv","sbahn")

```
There are three paramters for this function. 
| parameter-number | parameter-name | explanation | 
| ---------------- | -------------- | ----------- | 
| 1 | twitteraccount | is used for which twitter account will be used for searching in tweets. | 
| 2 | csvname | is a local cache file, to prevent one tweet multiple times | 
| 3 | vehicleType | declares which case should be used | 
