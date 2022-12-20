from datetime import date
import tweepy
import config  # has our tokens

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = "Ukrain OR Russia -is:retweet"  # query basically means what you are looking for
#if you want all tweets: "is:retweet"
#dont want : -is:retweet
#want tweets meadie : has:media
#ps : if you want to know more about searching on twitter go to developer.twitter.com -> Docs and you will find everything u want


response = client.search_recent_tweets(query=query,max_results=100,tweet_fields=['created_at','lang'], user_fields=['profile_image_url'], expansions=['author_id'])

# tweet_fields ile twitlerin atıldığı bölgeleri,atıldığı dilleri görebiliyoruz.
# search'te daha fazla şey öğrenmek istiyorsan developer.twitter.com -> Docs->Expansions ile araştırma filtreni genişletebilirsin.

users = {u['id']: u for u in response.includes['users']}
for tweet in response.data:
     if users[tweet.author_id]:
          user = users[tweet.author_id]
          print(user.profile_image_url)
          print(user.name)
          print(tweet.id)
#Buraya kadar SEARCH kısmıydı.

#get more than 100 tweet 
for tweet in tweepy.Paginator(client.search_recent_tweets,query=query,max_results=100).flatten(limit=1000000):
     print(tweet.id)

#tweetleri txt file yazdırma

file_name= 'tweets.txt'

with open(file_name,'a+') as fileHandler:
     for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000000):
          fileHandler.write('%s\n' % tweet.id)
#belirli bir zaman aralığında aratmak için

start_time = '2020-01-01T00:00:00Z'
end_time= '2020-10-06T00:00:00Z'

response = client.search_recent_tweets(query=query,max_results=100,start_time=start_time,end_time=end_time)

for tweet in response.data:
     print(tweet.id)


# belirli bir zaman aralığındaki tweet sayıları

