import json
import urllib,urllib2

class GoogleHandler:
  base = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'
  queryparam = 'q'

  def search(self,site,question):
    question = "site:"+site+" "+" ".join(question)
    query = urllib.urlencode({self.queryparam : question})
    response = urllib2.urlopen(self.base + query).read()
    datajson = json.loads(response)
    question_url = datajson['responseData']['results'][0]['url']

    question_id=[ int(word) for word in question_url.split('/') if word.isdigit() ][0]
    return question_id


class SearchEngineHandler:

  def __init__(self,site="google"):
    self.site=site
    if site=="google":
      self.handler=GoogleHandler()

  def search(self,site,question):
    self.handler.search(site,question)