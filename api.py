from __future__ import absolute_import, print_function
import logging
from os import write
from types import SimpleNamespace
from typing import Text
import tweepy
import telegram
import time

busline = 8800
sbahn = "S2"
telegramId = <TelegramID>
telegramBotID = <TelegramBotID>
consumer_key="<TwitterAPI ConsumerKey>"
consumer_secret="<TwitterAPI ConsumerSecret>"

access_token="<TwitterAPI Access Token>"
access_token_secret="<TwitterAPI Access Token Secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def notifyTelegram(headline, busmessage):
    """
    Notify my Telegram Bot
    """
    logging.info("Send Message via Telegram")
    bot = telegram.Bot(token=telegramBotID)
    bot.send_message(chat_id=telegramId, text=headline+busmessage,parse_mode=telegram.ParseMode.HTML)
    print("message send")

def generalSearchTwitterAPI(twitterAccount,csvname,vehicleType):
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    rawJsonTimeline = api.user_timeline(twitterAccount)
    headline = ''
    for i in range (20):
        hvvStoerungen = rawJsonTimeline[i]
        lineList = [line.rstrip('\n') for line in open(csvname)]

        if (hvvStoerungen["id_str"] in lineList):
                logging.debug("object in Cache found")
        else:
            print("nothing found")
            lineList.append(hvvStoerungen["id"])
            with open(csvname, 'a') as f:
                f.write("%s\n" % hvvStoerungen["id_str"])
            f.close()
            if vehicleType == "sbahn": 
                if sbahn in hvvStoerungen["text"]:
                    headline = "<b>SBahn:"+sbahn+"</b> - Störung \n"
                    busmessage = hvvStoerungen["text"]
                    notifyTelegram(headline,busmessage) 
            elif vehicleType == "bus":
                for hashtag in hvvStoerungen["entities"]["hashtags"]: 
                    if hashtag["text"] == "vhh"+str(busline):
                        headline = "<b>BUS:"+str(busline)+"</b> - Störung \n"
                        busmessage = hvvStoerungen["text"]
                        notifyTelegram(headline,busmessage)

if __name__ == '__main__':
    while True:
        generalSearchTwitterAPI("vhhbus","vhhbus.csv","bus")
        generalSearchTwitterAPI("HVVStoerungen","hvvStoerungen.csv","sbahn")
        time.sleep(600)     
