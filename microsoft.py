### API TO GET RELEVANT KEYWORDS FOR A MINISTRY ###

import http.client, urllib
import json

accessKey = '1f737f759c0d4d4689e41d34bf55d1c4'

uri = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/keyPhrases'

def GetKeyPhrases (documents):
    "Gets the sentiments for a set of documents and returns the information."
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = http.client.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'The Ministry of Minority Affairs was carved out of Ministry of Social Justice & Empowerment and created on 29th January 2006 to ensure a more focused approach towards issues relating to the notified minority communities namely Muslim, Christian, Buddhist, Sikhs, Parsis and Jain. The mandate of the Ministry includes formulation of overall policy and planning, coordination, evaluation and review of the regulatory framework and development programmes for the benefit of the minority communities.' },
    { 'id': '2', 'language': 'es', 'text': 'Si usted quiere comunicarse con Carlos, usted debe de llamarlo a su telefono movil. Carlos es muy responsable, pero necesita recibir una notificacion si hay algun problema.' },
    { 'id': '3', 'language': 'en', 'text': 'The Grand Hotel is a new hotel in the center of Seattle. It earned 5 stars in my review, and has the classiest decor I\'ve ever seen.' }
]}

print('Please wait a moment for the results to appear.\n')
result = GetKeyPhrases(documents)
print(json.dumps(json.loads(result), indent=4))