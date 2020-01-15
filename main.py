'''
Created on Jan 10, 2020

@author: rehme
'''
import os
import tweepy
import time
from generateText import generate




def main():

    tweetInterval = 60 * 60 *2 #Tweet every hour
    
    # Get credentials from environment variables set in OS or heroku
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    
    
    # Create API authentication object with tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Verify credentials and produce message indicating success 
    try:
        api.verify_credentials()
        print("Authentication successful")
    except:
        print("Authentication unsuccessful")
        return
    
    # The bot generates until stopped
    while True:
        print("generating message and sending to twitter...")
        
        randTweet = generate() # Generate text to tweet
        api.update_status(randTweet) # Tweet the text
        time.sleep(tweetInterval) # Wait for 8 hours to tweet again
        

if __name__ == '__main__':
    main()
    
    

    
