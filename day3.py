import requests
from bs4 import BeautifulSoup

hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
Url_main = "https://comic.naver.com"
sub_url_Weekday = "/webtoon/weekdayList.nhn?week="
days = ['mon','tue', "wed", "thu","fri","sat","sun"]
kr_day = ['월','화','수','목','금','토','일']
mainPage = requests.get(Url_main, headers = hdr)
soup = BeautifulSoup(mainPage.content, "html.parser")
#print(soup)

#main Thread
def main():
    for i in range(7):
        print(str(i+1)+". "+ kr_day[i], end=" ")
    print("\n요일 선택:")

main()