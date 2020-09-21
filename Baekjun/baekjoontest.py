import requests 
from bs4 import BeautifulSoup
import os
import time

# prob_num = str(input())
# url = "https://www.acmicpc.net/problem/" + prob_num
# req = requests.get(url)
# soup = BeautifulSoup(req.text,"html.parser")
# print(len(soup.select("pre.sampledata")))
# input_data = soup.select("pre.sampledata")
# output_data = soup.select("pre.sampledata")

class Baekjoon:
    def __init__(self,num):
        if not num is None:
            self.num = str(num)
            self.url = "https://www.acmicpc.net/problem/"+self.num
            self.req = requests.get(self.url).text
            self.soup = BeautifulSoup(self.req,"html.parser")

            

    def Len_check(self):
        length = int(len(self.soup.select("pre.sampledata")))
        return length
        
    def Parser(self):
        length_data = int(self.Len_check()/2)
        soup_data = self.soup.select("pre.sampledata")
        answer = {}

        # 샘플 데이터가 1개일 경우
        if (length_data) <2:
            input_data = soup_data[0].text.rstrip() # 이스케이프 문자 제거
            output_data = soup_data[1].text
            # answer = {soup_data.text.rstrip():soup_data[1].text for key,val in soup_data}
            answer[input_data] = output_data
            return answer

        #  샘플 데이터가 2개 이상인 경우
        else:          
            idx = 0
            for i in range(0,length_data):
                answer[soup_data[idx].text] = soup_data[idx+1].text
                idx += 2
            return answer

    # def File_Printer(self):
    #     file_name = os.path.basename(__file__)

        
    #     return os.path.splitext(file_name)[0]
    @
    
    @staticmethod
    def file_searcher(self,filepath):
        
        file_name = os.path.basename(filepath)
        title = os.path.splitext(file_name)[0]
        url = "https://www.acmicpc.net/search#q"+ title
        req = requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        div = soup.select("div.results")[0]
        highest_one = div.select_one("h3 > a > strong")
        print(highest_one)
        return highest_one
        
        
    
    def __str__(self):
        return self.num
# start = time.time()
# print(Baekjoon(6603).Parser())
# print(time.time()-start)
# file_name = str(__file__).split("/")
# print(file_name[-1])
# file_name = os.path.basename(__file__)
# print(os.path.splitext(file_name)[0])