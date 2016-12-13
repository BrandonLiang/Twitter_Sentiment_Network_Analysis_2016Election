from nltk.sentiment.vader import SentimentIntensityAnalyzer
import network
import nltk
import sys
import csv

sid = SentimentIntensityAnalyzer()
# result = []
# result.append(["Tweet","User","Compound","Negative","Neutral","Positive"])
filename = sys.argv[1]
finalname = sys.argv[2] # exlcuing ".csv"
hashtag = filename.split("_")[0]
file_ = open(finalname+".csv","wb")
writer = csv.writer(file_)
writer.writerow(["User","Original_User/Web","Compound","Negative","Neutral","Positive","Tweet"])
file = open(filename,"rb")
reader = csv.reader(file)
reader.next()
for line in reader:
	tweet = line[6].replace("\n","")
	print tweet
	ss = sid.polarity_scores(tweet)
	row = [line[1]]
	if ("@" in tweet):
		user_2 = tweet.split("@")[1].split(" ")[0].replace(":","")
		row.append(user_2)
		for k in sorted(ss):
			row.append(str(ss[k]))
		row.append(tweet)
		writer.writerow(row)
	row = [line[1]]
	web = nltk.word_tokenize(tweet)
	if ("https" in web):
		index = web.index("https")
		#print web
		try:
			website = web[index]+web[index+1]+web[index+2]
			if ("/" in website):
				print website
				host = network.find_host(website)
				row.append(host)
				for k in sorted(ss):
					row.append(str(ss[k]))
				row.append(tweet)
				writer.writerow(row)
		except:
			x = 1

file.close()
file_.close()


# users = {}
# webs = {}
# for line in reader:
# 	user = line[1]
# 	tweet = line[6].replace("\n","")

# 	#if ("https" in tweet):
	
			
# for key in users:
# 	writer.writerow([key,users[key]])
# for key in webs:
# 	writer.writerow([key,webs[key]])

# file.close() 
# file_2.close()