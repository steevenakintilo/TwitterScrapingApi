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


l = ["https://twitter.com/AS_Monaco/status/1679883454438326274",
        "https://twitter.com/ReyesClothes/status/1680277758193160193",
        "https://twitter.com/JennyyOfficiel/status/1680210543716515840",
        "https://twitter.com/MercaFoot_/status/1680155267328102401",
        "https://twitter.com/conkerax/status/1678835904935256066"]

rl = [
    "https://twitter.com/user/status/1672185238863355904",
    "https://twitter.com/user/status/1672152816268328961",
    "https://twitter.com/user/status/1672152514526052354",
    "https://twitter.com/user/status/1671932383963103242",
    "https://twitter.com/user/status/1671926761959964715",
    "https://twitter.com/user/status/1671895836203315205",
    "https://twitter.com/user/status/1671593832138547200",
    "https://twitter.com/user/status/1671564767436079105",
    "https://twitter.com/user/status/1671554308561567744",
    "https://twitter.com/user/status/1671534460699828224",
    "https://twitter.com/user/status/1671526984579534850",
    "https://twitter.com/user/status/1671475617236238337",
    "https://twitter.com/user/status/1671473043632168960",
    "https://twitter.com/user/status/1671461708697862146",
    "https://twitter.com/user/status/1671444344056995840",
    "https://twitter.com/user/status/1671436034851176450",
    "https://twitter.com/user/status/1671433878039408641",
    "https://twitter.com/user/status/1671427741294419971",
    "https://twitter.com/user/status/1671425218139639808",
    "https://twitter.com/user/status/1671229615254143066",
    "https://twitter.com/user/status/1671213771023319052",
    "https://twitter.com/user/status/1671211051424022555",
    "https://twitter.com/user/status/1671201242788376599",
    "https://twitter.com/user/status/1671171297781633024",
    "https://twitter.com/user/status/1671162512983879689",
    "https://twitter.com/user/status/1671133863299497984",
    "https://twitter.com/user/status/1671122001577099264",
    "https://twitter.com/user/status/1671121484146786304",
    "https://twitter.com/user/status/1671035150027853824",
    "https://twitter.com/user/status/1671029283635056641",
    "https://twitter.com/user/status/1670903519597977600",
    "https://twitter.com/user/status/1670877177322012672",
    "https://twitter.com/user/status/1670875962916098048",
    "https://twitter.com/user/status/1670838854222479363",
    "https://twitter.com/user/status/1670809033165381632",
    "https://twitter.com/user/status/1670797693587714058",
    "https://twitter.com/user/status/1670790976737099786",
    "https://twitter.com/user/status/1670725999196094464",
    "https://twitter.com/user/status/1670657665377206272",
    "https://twitter.com/user/status/1670506667258126336",
    "https://twitter.com/user/status/1670505620980617217",
    "https://twitter.com/user/status/1670491817752805376",
    "https://twitter.com/user/status/1670458966361374727",
    "https://twitter.com/user/status/1670370854226612224",
    "https://twitter.com/user/status/1670130094340276224",
    "https://twitter.com/user/status/1670109046672699395",
    "https://twitter.com/user/status/1670106038802997259",
    "https://twitter.com/user/status/1670010300223954947",
    "https://twitter.com/user/status/1670010211858370561",
    "https://twitter.com/user/status/1670008387030114307",
    "https://twitter.com/user/status/1672682218001498112",
    "https://twitter.com/user/status/1672664972420173825",
    "https://twitter.com/user/status/1672647294535999490",
    "https://twitter.com/user/status/1672285424931282945",
    "https://twitter.com/user/status/1672273570494312448",
    "https://twitter.com/user/status/1672258219102834690",
    "https://twitter.com/user/status/1672256277961949186",
    "https://twitter.com/user/status/1672236098741829632",
    "https://twitter.com/user/status/1672193445866110977",
    "https://twitter.com/user/status/1671932464451797011",
    "https://twitter.com/user/status/1671915703497048064",
    "https://twitter.com/user/status/1671913691896217602",
    "https://twitter.com/user/status/1671864873226051585",
    "https://twitter.com/user/status/1671843009653080064",
    "https://twitter.com/user/status/1671840121400770560",
    "https://twitter.com/user/status/1671804570996187137",
    "https://twitter.com/user/status/1671557437579460611",
    "https://twitter.com/user/status/1671520531336556548",
    "https://twitter.com/user/status/1671495248495738882",
    "https://twitter.com/user/status/1671470705655836673",
    "https://twitter.com/user/status/1671469712855781381",
    "https://twitter.com/user/status/1671258754330030082",
    "https://twitter.com/user/status/1671120254200688643",
    "https://twitter.com/user/status/1671107262696267776",
    "https://twitter.com/user/status/1671095555144175618",
    "https://twitter.com/user/status/1671095233851928577",
    "https://twitter.com/user/status/1671066892163842049",
    "https://twitter.com/user/status/1670889664851374095",
    "https://twitter.com/user/status/1670847722721624065",
    "https://twitter.com/user/status/1670831822303907841",
    "https://twitter.com/user/status/1673364450039021580",
    "https://twitter.com/user/status/1673352920748679168",
    "https://twitter.com/user/status/1673013930724130816",
    "https://twitter.com/user/status/1673011212148264963",
    "https://twitter.com/user/status/1672942924156264450",
    "https://twitter.com/user/status/1672894312843997184",
    "https://twitter.com/user/status/1672642495396577282",
    "https://twitter.com/user/status/1672533781276770304",
    "https://twitter.com/user/status/1672326393877745666",
    "https://twitter.com/user/status/1670831232400211972",
    "https://twitter.com/user/status/1670804742560251907",
    "https://twitter.com/user/status/1670796980870676484",
    "https://twitter.com/user/status/1670763620127371265",
    "https://twitter.com/user/status/1670761441719205889",
    "https://twitter.com/user/status/1670761143718096898",
    "https://twitter.com/user/status/1670684420058259456",
    "https://twitter.com/user/status/1673361248338034689",
    "https://twitter.com/user/status/1673361130272575488",
    "https://twitter.com/user/status/1673326499296866305",
    "https://twitter.com/user/status/1673302869536133121"
]

def main():
    S = start_api()
    print("Starting Bot")
    #unlike_a_tweet(S,"https://twitter.com/PiccoDamayonaiz/status/1674688012448583684")
    #comment_a_tweet(S,"https://twitter.com/PiccoDamayonaiz/status/1674688012448583684","toto",False,"")
    #unlike_a_tweet(S,"https://twitter.com/PiccoDamayonaiz/status/1674688012448583684")
    #like_a_tweet(S,"https://twitter.com/PiccoDamayonaiz/status/1674688012448583684")
    
    #unlike_a_tweet(S,"https://twitter.com/PiccoDamayonaiz/status/1674688012448583684")
    #get_list_of_following(S,"twiiiiter7")
    #check_if_user_follow(S,"twiiiiter7")
    #reetweet_a_tweet(S,"https://twitter.com/ZinoToujours/status/1681000213786361857")
    #make_a_tweet_with_pool(S,"hello my name is bob 👍",4,"1","2","3","4",7,23,59)
    #make_a_tweet_with_pool(S,"hello my name is bob 👍",4,"1","2","3","4",6,23,59)

    #idx = 0
    #get_mentions(S,50)
    idx = 0

    search_q = search_tweet(S,"hello","recent",100)
    for s in search_q:
        print(s)
    quit()
    tweet_list2 =  get_list_of_user_tweet_url(S,"mediavenir",100)
    print("toto 2")
    
    print(len(tweet_list2))
    for t in tweet_list2:
        print(t)
    quit()
    print("###########################################")
    for t in tweet_list1:
        print("rt rt rt " , t)
        print(len(tweet_list1))
    
    quit()
    print("###########################################")
    
    for t in tweet_list2:
        print("twt twt twt " , t)
        print(len(tweet_list2))
    
    print("###########################################")
    
    for t in tweet_list3:
        print("cmt cmt cmt " , t)
        print(len(tweet_list3))
    
    # tweet_list = get_list_of_all_tweet_withouth_rt(S,"mediavenir",33)
    # #idx = 0
    # #get_mentions(S,50)
    # idx = 0
    # for t in tweet_list:
    #     idx+=1
    #     print("tweet by mediavenir " , t , " toto " , idx)

    
    # time.sleep(3)
    
    # print("##########################################################")
    # tweet_list = get_list_of_all_tweet_withouth_rt(S,"alertesinfos",33)
    # #idx = 0
    # #get_mentions(S,50)
    # idx = 0
    # for t in tweet_list:
    #     idx+=1
    #     print("tweet by alertesinfos " , t , " toto " , idx)
    # print("##########################################################")
    # print("ok")
    # #print(tweet_list)
    #for t in tweet_list:
    #    idx+=1
    #    print("##### link: " + t , " nb of tweet found: " , idx , " #####")
    #for r in l:
    #    print(check_if_tweet_retweet(S,r))
    #    bookmark_a_tweet(S,r)
    #toto = check_if_tweet_retweet(S,"https://twitter.com/Twiiiiter7/status/1681065958721347585")
    #print("liked or not " , toto)
    #print(get_tweet_info(S,"https://twitter.com/betatesteu76030/status/1681408194550087693"))
    #print(get_tweet_info(S,"https://twitter.com/PiccoDamayonaiz/status/1674688012448583684"))
    #for r in l:
    #    print(get_tweet_info(S,r))
    quit()
    exit()
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