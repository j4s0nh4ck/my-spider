import requests
from bs4 import BeautifulSoup
from time import sleep
from pprint import pprint
session = requests.Session()


###############################################################################
# GET headers/cookies from brwoser after login
###############################################################################
headers = {
    'Host': "www.zhihu.com",
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv: 40.0) Gecko/20100101 Firefox/40.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "en-US,en;q=0.5",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive"
}
cookies = {
    '__utma': "51854390.1062397664.1442369425.1442369425.1442371688.2",
    '__utmb': "51854390.14.10.1442371688",
    '__utmc': "51854390",
    '__utmt': "1",
    '__utmv': "51854390.100--|2=registration_date=20150503=1^3=entry_date=20150503=1",
    '__utmz': "51854390.1442369425.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)", 
    '_xsrf': "b5b26676da98d77493373b8966394c9e",
    '_za': "50fb0c48-110c-4732-bc49-c4995e63a1d7",
    'cap_id': "MjNjNTE4YWNjZGQ5NDU3Yjg3ZmIyMzgzZTYxYTU1YTQ=|1442372350|d5e0b6ad39eff866a7337f20799a74787c6c26a3",
    'q_c1': "c74ebf04f34c4cbba8503e42f0a4a9de|1442369524000|1442369524000",
    'unlock_ticket': "QUJEQWtmdUtCZ2dYQUFBQVlRSlZUVWZpLUZYbERhRzhLTmY4ODJtekNRT200TGNVdUxmT3JBPT0=|1442372415|e6e97f452da25743cac6f056aa974eacf65ff02d",
    'z_c0': "QUJEQWtmdUtCZ2dYQUFBQVlRSlZUZFpvSUZhQjRWaWRiUi1IQkR4RGVSWVRhdGZ2b0pfQVBnPT0=|1442372566|9c91eee52e881649a4007bb3086a21ef1cfb4de8"
}
site = "www.zhihu.com"
touchUrl = 'http://www.zhihu.com/lastread/touch'
###############################################################################
# GET params within url 'http: //www.zhihu.com/explore', after hanover to button line
###############################################################################
params={
    'items': '[["answer","63776265","touch"],["answer","63738611","touch"]]', 
    '_xsrf': "b5b26676da98d77493373b8966394c9e"
}

def form_url(site, url): 
  return "%s%s" %(site, url)

rsp = session.get('http://www.zhihu.com/explore', headers=headers, cookies=cookies)
# print(rsp.text)
bs = BeautifulSoup(rsp.text, "lxml")
# pprint(bs.findAll('a', {"class": "question_link"}))
elems = bs.findAll('a', {"class": "question_link"})
for ele in elems: 
  print("title: %s\turl: %s" %(ele.text, form_url(site, ele.attrs['href'])))

for i in range(1,21): 
  pprint("#" * 30)
  cnt = i * 5
  sleep(5)
  rsp = session.post(touchUrl, params, headers=headers, cookies=cookies)
  url = 'http://www.zhihu.com/node/ExploreAnswerListV2?params={"offset": %d,"type": "day"}' % cnt
  rsp = session.get(url, headers=headers, cookies=cookies)
#  print("GET more response Code as: \t%d" %rsp.status_code)
  bs = BeautifulSoup(rsp.text, "lxml")
  elems = bs.findAll('a', {"class": "question_link"})
  for ele in elems:
    print("title: %s\turl: %s" % (ele.text, form_url(site, ele.attrs['href'])))
#  print("\n\n\n\n")
