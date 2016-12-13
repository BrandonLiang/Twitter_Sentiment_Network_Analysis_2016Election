import sys
import csv

filename = sys.argv[1]
file_ = open(filename,"rb")
reader = csv.reader(file_)
file__ = open("Html_"+filename[:-4]+".txt","w")

reader.next()
counter = 0
node2 = ""
for line in reader:
	if (counter != 0 and node2 != "" and node2 != "twitter" and node2 != "t"):
		file__.write(string)
	node1 = line[0]
	node2 = line[1]
	score = float(line[2])
	if (-1.0 <= score and score < -0.6):
		group = "1"
	elif (-0.6 <= score and score < -0.2):
		group = "2"
	elif (-0.2 <= score and score < 0.2):
		group = "3"
	elif (0.2 <= score and score < 0.6):
		group = "4"
	else:
		group = "5"
	string = "[\""+node1+"\",\""+node2+"\",\""+group+"\"],\n"
	counter = counter + 1
string = "[\""+node1+"\",\""+node2+"\",\""+group+"\"]"
file__.write(string)
file_.close()
file__.close()