import tweepy
import sys
import json
import csv

consumer_key = "T28J24MRSjEpa9Q6H0ukc0sbu"
consumer_secret = "f2eKWzkfSP1Ezg3qp79Ae45hlrycSeHIEKQeNEim8nJpYZHQnH"

access_token = "187087019-wY4yjLV1FIcORrUIsrwss9lzvOX5jTkIrFykVysH"
access_token_secret = "qXdxXAMkV4SZ7UVhmxIT0HvIjmNUGn8njuU7ofezkQIcR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
# for tweet in public_tweets:
# 	text = tweet.text.encode('ascii', 'ignore')
# 	print text

# user = api.get_user('BrandonLTruth')

# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#    print friend.screen_name

hashtag = sys.argv[1]
#date_since = sys.argv[2]
#date_until = sys.argv[3]
#max_count = int(sys.argv[4])

#file_ = open("#"+hashtag+"_from " + date_since + " to " + date_until + ".csv","wb")
file_ = open("#"+hashtag+".csv","wb")
writer = csv.writer(file_)
writer.writerow(["User","Username","User Description","Followers Count","Friends Count","Time","Tweet","Location","Retweeted Tweet","Retweet Count","Fav Count"])

for tweet in tweepy.Cursor(api.search,q=hashtag).items(): #,since=date_since,until=date_until,lang="en").items():
	t = json.loads(json.dumps(tweet._json))
	print t
	#break
	row = []
	row.append(t['user']['name'].encode('ascii','ignore'))
	row.append(t['user']['screen_name'].encode('ascii','ignore'))
	row.append(t['user']['description'].encode('ascii','ignore'))
	row.append(t['user']['followers_count'])
	row.append(t['user']['friends_count'])
	row.append(t['created_at'].encode('ascii','ignore'))
	row.append(t['text'].encode('ascii','ignore'))
	row.append(t['user']['location'].encode('ascii','ignore'))
	if "RT @" in t['text'].encode('ascii','ignore'):
		retweeted = "Yes"
	else:
		retweeted = "No"
	row.append(retweeted)
	row.append(t['retweet_count'])
	row.append(t['favorite_count'])
	writer.writerow(row)
file_.close()
# text, author.location,author.screen_name
