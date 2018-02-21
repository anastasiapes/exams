import datetime
import urllib2
import json

def samepicks(a,b):
	p1 = 0
	p2 = 0
	for i in range (0,10):
		for j in range (0,20):
			if a[i] == b[j]:
				p2 +=1
	if p2 > 4:
		p1 +=1
	return p

c= []
while True:
	flag = True
	x = raw_input("Enter 10 different numbers [1-80] :")
	picks = x.split(",")
	if len(picks)==10:
		for i in xrange(10):
			if flag == True:
				picks[i]=int(picks[i])
		for i in range(0,8):
			if flag== False:
				break
			for j in range(i+1,10):
				if picks[i] == picks[j]:
					flag = False
					print "The numbers must be different"
					break
			if flag==False:
				break
		for i in range (0,10):
			if flag == False:
				break
			if picks[i]>80 or picks[i]<1:
				flag = False
				print 'The numbers must be between 1 and 80'
				break

		if flag :
			break
	else:
		print 'Something went wrong, try again'


cur_date1 = datetime.datetime.now()
fcur_date = datetime.datetime.now()
fcur_date = fcur_date - datetime.timedelta(days=1)

for i in range (31):
	cur_date1 = cur_date1 - datetime.timedelta(days=1)
	date_format= cur_date1.strftime("%d-%m-%Y")
	url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_format
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data = json.loads(data)
	klhrwseis = data['draws']['draw']
	p = 0
	for i in klhrwseis:
		temp = i["results"]
		p += samepicks(picks,temp)
	c.append(p)
max = max(c)
for i in range (len(c)):
	if c[i] == max:
		time = fcur_date - datetime.timedelta(days=i)
print "The winning day is:"
print [time.weekday()],time.strftime('%d-%m-%Y')
