from src.start import *
from src.scrapper import *

def main():
    S = start_api()
    make_a_tweet(S,"hello world")

    t = "https://twitter.com/TwitterDev/status/1661790253886177280"
    
    comment_a_tweet(S,t,"My api is better ...",)
    S = [get_tweet_nb_of_bookmark(S,t),
    get_tweet_nb_of_like(S,t),
    get_tweet_nb_of_quote(S,t),
    get_tweet_nb_of_retweet(S,t),
    get_tweet_nb_of_view(S,t),
    get_tweet_text(S,t),
    get_tweet_user(S,t)]
    
    for s in S:
        print(s)