# JTP
- 기간 : 2022.08(일주일간)
- 데이터분석(파이썬)
- 참여인원: 3명

## 배경
1. 제주도내 비슷한 포지션을 가진 소품샵을 분석 의뢰
2. 유사 업종 간 차별화를 위한 포지션 이해 및 분석

## 설계
- 도내 소품샵에 대한 인지도, 상품, 포지션, 고객의 반응 등을 조사하기 위해서 웹크롤링 실시
- 주 고객층인 젊은 층에 대한 반응을 분석하기 위해 가장 잘 활용 되고 있는 인스타그램과 유튜브를 웹크롤링 대상으로 선정
- 본인은 유튜브 크롤링을 담당함

## 분석
1. selenium을 사용해 동적으로 검색어를 입력한 후 해당페이지의 parser 

```Python

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
```

2. 해당 영상의 기록을 추출하여 csv파일로 저장
```Python
df_just_video = pd.DataFrame(columns=['영상제목', '채널명', '영상url', '조회수', '영상등록날짜','구독자수'])

    df_just_video['영상제목'] = df_title
    df_just_video['채널명'] = df_writer
    df_just_video['영상url'] = df_link
    df_just_video['조회수'] = df_view
    df_just_video['영상등록날짜'] = df_date
    df_just_video['구독자수'] = df_subcount

    df_just_video.to_excel('C:/Users/mikae/OneDrive/바탕 화면/youtube/'+feature+'.xlsx', encoding='utf-8-sig', index=False)
    display(df_just_video)
```

3. 크롤링 결과를 csv로 모아  분석


## 배운점
 - 웹크롤링 라이브러리인 selenium과 beautifulSoup에 대한 이해도가 높아짐.
 selenium은 웹을 돌아다니는 것이고 beautifulSoup는 해당 페이지(html)에 대한 parser을 수집한느 것이라고 보면 됨.
 
 - 업무가 주어지고 팀원과 함께 분석 방법에 대해서 이야기하며 분석에 대한 전반적인 이해가 상승함. 
 
 - 배우기만 한 웹 크롤링을 직접 사용해보는 경험을 통해서 웹(html)에 대한 전반적인 지식도 습득하게 됨.
 
 
