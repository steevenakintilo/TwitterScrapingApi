from src.start import *
from src.scrapper import *

def dmain():
    print("maaaaaain")
    S = start_api()
    #make_a_tweet(S,"hello world")

    tweet_url = "https://twitter.com/TwitterDev/status/1661790253886177280"
    user_accont = "TwitterDev"
    #comment_a_tweet(S,t,"My api is better ...")

    #quote_a_tweet(S,tweet_url,"MMerci Elon Pour Les Travauxxxxxxx",False,r"")
    #comment_a_tweet(S,tweet_url,"daad",False,r"")
    #delete_a_tweet(S,"https://twitter.com/betatesteu76030/status/1673959249565581314")
    #get_tweet_info(S,tweet_url)
    tweet_list = [tweet_url]
    user_list = ["TwitterDev","Mediavenir","Twiiiiter7","Sangokuhomer201"]
    #unfollow_an_account(S,"colinlebedev")
    
    
    mention_url , mention_text = get_mention(S)
    
    
    print("OoOoOoOoOoOoOoO")
    print(mention_url[0])
    print(mention_text[0])
    print("OoOoOoOoOoOoOoO")
    
    
    
    #get_tweet_info(S,"https://twitter.com/PiccoDamayonaiz/status/1674688012448583684")
    #print("https://twitter.com/oggy_oggy_t/status/1674559930982858752")
    #print(get_tweet_info(S,mention_url[0]))
    a = 19
    if a == 9:

        for text in mention_text:
            print(text)
            #t = text.split("@betatesteu76030")
            #print(str(t[1]).split("\n"))
            
        for url in mention_url:
            print(url)
            
        #TweetInfo = get_tweet_info(S,tweet_url)
        
        #UserInfo = get_user_info(S,user_accont)
        #UserNbOfMedia = get_user_number_of_media(S,user_accont)
        #UserNbOfLike = get_user_number_of_like(S,user_accont)
        

        print("TweetInfo")
        for x in mention_url:
            print("xxx " , x)
            TweetInfo = get_tweet_info(S,x)
            for key in TweetInfo:
                print(key, ":", TweetInfo[key])
            print("########################################")
            pass
        print("TweetInfo")
        
        print("UserList")
        
        for x in user_list:
            UserInfo = get_user_info(S,x)
            for key in UserInfo:
                print(key, ":", UserInfo[key])
            print("Number of like: ", get_user_number_of_like(S,x))
            print("Number of media: ", get_user_number_of_media(S,x))
            print("########################################")
        #     pass
        print("UserList")
        
    print("Done Done")


def main():
    S = start_api()
    print("Staeting Bot")
    l_url = []
    idx = 0
    while True:
        idx = idx + 1
        mention_url , mention_text = get_mention(S)
        mention_url.reverse()
        mention_text.reverse()
        for i in range(len(mention_url)):
            m_text = mention_text[i]
            m_url = mention_url[i]
            if "luffy" in m_text and m_url not in l_url:
                print("luuuuuuuuuuufy")
                comment_a_tweet(S,m_url,"MOOOOOOonkey D lufuuuuuuuuuzy",False,"")
                l_url.append(m_url)
                time.sleep(40)
            elif "goku" in m_text and m_url not in l_url:
                print("gooooooooooooooooku")
                comment_a_tweet(S,m_url,"Goatooooooooooooooku le bg",False,"")
                l_url.append(m_url)
                time.sleep(40)
            elif "naruto" in m_text and m_url not in l_url:
                print("narutoooooooooooo")
                comment_a_tweet(S,m_url,"le goat naruuuuuuuuuuuuuuuuuuuuuuuto",False,"")
                l_url.append(m_url)
                time.sleep(40)

            #print(m_text)
            #print(m_url)
        print("#"*50)
        print(idx)
        time.sleep(300)