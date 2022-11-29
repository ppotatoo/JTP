from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import time
from IPython.display import display
import warnings
from openpyxl import Workbook

warnings.filterwarnings(action='ignore')

path = 'C:/Users/mikae/Downloads/chromedriver_win32 (3)/chromedriver.exe'
def get_video():
    feature = '테라로사 서귀포점'

    driver = webdriver.Chrome(path)
    driver.get('https://www.youtube.com')

    n = 3
    while n > 0:
        print('웹페이지를 불러오는 중입니다..' + '..' * n)
        time.sleep(1)
        n -= 1

    src = driver.find_element_by_xpath('//*[@id="search"]')
    src.send_keys(feature)
    src.send_keys(Keys.RETURN)

    n = 2
    while n > 0:
        print('검색 결과를 불러오는 중입니다..' + '..' * n)
        time.sleep(1)
        n -= 1

    print('데이터 수집 중입니다....')

    html = driver.page_source
    soup = BeautifulSoup(html)


    # 스크롤 다운
    body = driver.find_element_by_tag_name('body')
    num_of_pagedowns = 5
    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        num_of_pagedowns -= 1


    df_title = []
    df_link = []
    df_writer = []
    df_view = []
    df_date = []
    df_subcount = []

    total = len(soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated'))
    for i in range(len(soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated'))):
        title = soup.find_all('a', {'id': 'video-title'})[i].text.replace('\n', '')
        link = 'https://www.youtube.com/' + soup.find_all('a', {'class': 'style-scope ytd-video-renderer'})[i]['href']
        writer = \
        soup.find_all('ytd-channel-name', 'long-byline style-scope ytd-video-renderer')[i].text.replace('\n', '').split(
            ' ')[0]
        view = \
        soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated')[i].text.split('•')[
            1].split('\n')[3]
        date = \
        soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated')[i].text.split('•')[
            1].split('\n')[4]

        df_title.append(title)
        df_link.append(link)
        df_writer.append(writer)
        df_view.append(view)
        df_date.append(date)

    driver.close()


    #구독자수
    driver = webdriver.Chrome(path)
    for button in range(total):
        driver.get(df_link[button])
        num = driver.find_element_by_xpath('//*[@id="subscriber-count"]').text
        df_subcount.append(num)
    driver.close()

    df_just_video = pd.DataFrame(columns=['영상제목', '채널명', '영상url', '조회수', '영상등록날짜','구독자수'])

    df_just_video['영상제목'] = df_title
    df_just_video['채널명'] = df_writer
    df_just_video['영상url'] = df_link
    df_just_video['조회수'] = df_view
    df_just_video['영상등록날짜'] = df_date
    df_just_video['구독자수'] = df_subcount

    df_just_video.to_excel('C:/Users/mikae/OneDrive/바탕 화면/youtube/'+feature+'.xlsx', encoding='utf-8-sig', index=False)
    display(df_just_video)
    # else:
    #     return '프로그램을 종료합니다.'

get_video()