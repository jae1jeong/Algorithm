from baekjoontest import Baekjoon
import os
import requests
from bs4 import BeautifulSoup
from urllib import parse
# N = int(input())
# lst = list(map(int, input().split(" ")))
# print(max(lst)-min(lst))


# a = Baekjoon(None).file_searcher(__file__)


file_name = os.path.basename(__file__).split(".")[0]

# soup = BeautifulSoup(req,"html.parser")
# print(soup.text)
# div = soup.select("div.results")[0]
# highest_one = div.select_one("h3 > a > strong")
# # print(highest_one)
data = {
"id": "1670563073163149",
"ev": "PageView",
"dl": "https://www.acmicpc.net/search#q=%EB%8F%99%EB%AC%BC%EC%9B%90&c=Problems",
"rl": "https://www.acmicpc.net/",
"ts": "1589310992002",
"if":"false",
"sw": "1920",
"sh": "1080",
"v": "2.9.18",
"r": "stable",
"ec": "31",
"o": "30",
"fbp": "fb.1.1587198902611.538505270",
"it": "1589310919725",
"coo": "false",
"rqm": "GET"
}
# req= requests.get("https://www.acmicpc.net/search#q=" + file_name+"&c=Problems",data)
# print(req.text)
url = parse.urlparse("https://www.acmicpc.net/search#q=" + str(file_name)+"&c=Problems")

a = parse.parse_qs(url.query)
print(a)