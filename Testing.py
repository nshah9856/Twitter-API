import tweepy
import time

KEY = "XdJ4a3GiYBgcAgJae88HgMsX9"
SECRET = 'H8geeOUQfG4fYUl3H49okuLJXmul33ViTOextsT7LngPlChaGO'
AC_TOKEN = '2950936730-Qhy9qH1A89r3Qv4gQO1Zv8Cr0p7J9fpqKkfIix9'
AC_SECRET = 'REWFrIHqzhO59mFjuKmFFPeGG6wMm2v6bKtxt04Yo5FF0'



auth = tweepy.OAuthHandler(KEY, SECRET)
auth.set_access_token(AC_TOKEN, AC_SECRET)

api = tweepy.API(auth)

# api.create_friendship('@npshah9856')    # Follows the user specified

# api.update_with_media('C:\\UCI\\My Projects\\Twitter Api\\image.jpg','Admire and save the nature!') # Filename first and then the text -- updates status

# api.update_profile_image('C:\\UCI\\My Projects\\Twitter Api\\image.jpg') #Changes the profile picture

# for i in api.followers():
#     print(i._json['name'])

def foo():
    us = input('Enter the user id: \n')
    x = api.send_direct_message(user=us, text=input('Enter the message: \n'))

    print('sent')

    return
#
#     for i in api.direct_messages(since_id = x.id)():#  Work on this pleasee I need to stream so, when I get a direct message I can display it and respond from it directly from here...
#         print(i.text)
#     return
#


def AnalyzingTweet(status):
    tw = "tweet :: " + status.text
    us = "user  :: " + status.user.name

    return tw,us

def GettingMessage(status):
    user = status[status.find("name")+6:status.find("screen_name")-2].strip('"')
    text = user + 'sent::' + status[status.find("text")+6:status.find("sender")-2].strip('"')
    return text
class MyStreamListener(tweepy.StreamListener):
    def on_friends(self, friends):
        print(friends)
    def on_direct_message(self, status):
        print(GettingMessage(status))

        return True
    def on_status(self, status):

        an = AnalyzingTweet(status)
        print(an)
        return True
    def on_data(self,status):
        self.on_direct_message(status)
        foo()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

# myStream.filter(track=['@nshah9856'])
##myStream.userstream()
# Send a specified direcet message to the specified user



# Gets the tweets from the specified time line and displays it

while True:
    public_tweets = api.user_timeline(id="@realDonaldTrump")
##    print(public_tweets)
    for tweet in public_tweets:
##        print(tweet)
        print(tweet.text, '\n')
        if input("Enter 'Y' to continue accessing other users :): ") == 'Y':
            continue
        else:
            print('Bye!')
            break

