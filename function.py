import operator
import json

def getMinistry(description):
	keywords = json.loads(open('keywords').read())
	m = {}
	ct = {}
	for ministry in keywords:
		ct[ministry] = 0
		mywords = keywords[ministry]
		for word in mywords:
			m[word] = ministry
	words = description.split()
	for word in words:
		try:
			ct[m[word]] += 1
		except:
			pass
	return max(ct, key=ct.get)
	# return max(ct.iteritems(), key=operator.itemgetter(1))[0]