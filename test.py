from src.start import *
from src.scrapper import *

def main():
    S = start_api()
    #make_a_tweet(S,"hello world")

    tweet_url = "https://twitter.com/TwitterDev/status/1661790253886177280"
    user_accont = "TwitterDev"
    #comment_a_tweet(S,t,"My api is better ...")
    TweetInfo = [get_tweet_nb_of_bookmark(S,tweet_url),
    get_tweet_nb_of_like(S,tweet_url),
    get_tweet_nb_of_quote(S,tweet_url),
    get_tweet_nb_of_retweet(S,tweet_url),
    get_tweet_nb_of_view(S,tweet_url),
    get_tweet_text(S,tweet_url),
    get_tweet_user(S,tweet_url)]
    
    UserInfo = [get_user_bio(S,user_accont),
    get_user_date_account_create(S,user_accont),
    get_user_nb_of_follower(S,user_accont),
    get_user_nb_of_following(S,user_accont),
    get_user_number_of_like(S,user_accont),
    get_user_number_of_tweet(S,user_accont),
    get_user_username(S,user_accont),

    ]

    print("TweetInfo")
    for tweet in TweetInfo:
        print(tweet)
    print("TweetInfo")
    
    print("UserInfo")
    for user in UserInfo:
        print(user)
    print("UserInfo")
    