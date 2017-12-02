import operator
import json

keywords = {
"Ministry of Home Affairs" : ["unidentified","object"],
"Ministry of Railways" : ["track","broken"],
"Ministry of Tourism" : ["monument"]
}

def getMinistry(description):
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
