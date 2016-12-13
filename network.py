import csv
import os
import sys
from bs4 import BeautifulSoup
from urllib import urlopen
import requests

def find_host_helper(url):
	lst = url.split("//")[1].split("/")[0].split(".")
	if lst[0] == "www":
		return lst[1]
	else:
		return lst[0]

def find_host(link):		
	api = "http://www.linkexpander.com/?url="
# filename = sys.argv[1]

# file_ = open(filename,"rb")
# reader = csv.reader(file_)
# file__ = open("updated_"+filename,"wb")
# writer = csv.writer(file__)
# for line in reader:
	#if ("https" in line[1]):
		#link = line[1]
	url = api + link
	print url,
		# #break
		# # print link
	try:
		html = urlopen(link)
			# print html.getcode()
			# response = requests.get(url)
		print find_host_helper(html.url)
		return find_host_helper(html.url)
	except:
		return ""
		#break
		# soup = BeautifulSoup(html).findAll("link")
		# for a in soup:
		# 	print a
		# 	break
		#break
		# # if ("script src" in soup):
		# # 	print soup.split("script src")[1].split(" ")[0]
		# #print link
		# s = str(soup[0].extract())
		# try:
		# 	print s.split("host=")[1].split(";")[0]
		# except:
		# 	print s
# 		# break
# 	writer.writerow(line)

# file_.close()
# file__.close()


