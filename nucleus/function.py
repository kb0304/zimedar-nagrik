import operator
import json

keywords = {
"Ministry of Home Affairs" : ["unidentified","object","bomb","terrorist"],
"Ministry of Railways" : ["track","broken","late","train","station","ticket","railway"],
"Ministry of Tourism" : ["monument","spit","crowd"],
"Traffic Police" : ["traffic","jam","light","speed","breaker"],
"Local Police" : ["accident","theft","thief","crash","steal"]
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
			ct[m[word.lower()]] += 1
		except:
			pass
	ministries = list(ct.keys())
	result = ministries[0]
	for possible in ministries:
		if ct[possible] > ct[result]:
			result = possible
	return result
#	return max(ct, key=ct.get)
