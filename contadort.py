# coding=utf-8
import tweepy
import time, os, datetime
from credent import *

MY_USER = 'nachoad'

def to_emoji(num_to_emoji):
    if num_to_emoji==0:
        return "0️⃣"
    elif num_to_emoji==1:
        return "1️⃣"
    elif num_to_emoji==2:
        return "2️⃣"
    elif num_to_emoji==3:
        return "3️⃣"
    elif num_to_emoji==4:
        return "4️⃣"
    elif num_to_emoji==5:
        return "5️⃣"
    elif num_to_emoji==6:
        return "6️⃣"
    elif num_to_emoji==7:
        return "7️⃣"
    elif num_to_emoji==8:
        return "8️⃣"
    elif num_to_emoji==9:
        return "9️⃣"




def main():
    ### Access and authorize credentials
    auth = tweepy.OAuthHandler(ck, cs)
    auth.set_access_token(at, ats)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Obtenemos el numero de followers de la cuenta de Twitter
    user = api.get_user(MY_USER)
    num_followers = user.followers_count
    print ("followers: "+ str(num_followers))

    # Comprobamos con el num anterior
    f = open("actual.txt", "r")
    actual=f.read()
    f.close()

    if int(actual) != num_followers:
        millares = num_followers // 1000
        tmp = num_followers % 1000
        centenas = tmp // 100
        tmp = tmp % 100
        decenas = tmp // 10
        unidades = tmp % 10

        print ("millares: " + str(millares))
        print ("centanas: " + str(centenas))
        print ("decenas: " + str(decenas))
        print ("unidades: " + str(unidades))

        emoji_followers = " 👉 "+ to_emoji(millares)+ to_emoji(centenas)+ to_emoji(decenas)+ to_emoji(unidades)
        name = "Nacho Alonso"
        new_name = name + emoji_followers
        print(new_name)

        api.update_profile(name=new_name)

        f = open ("actual.txt", "w+")
        f.write(str(num_followers))
        f.close()




if __name__ == '__main__':
    main()
