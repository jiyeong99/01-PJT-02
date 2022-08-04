# 프로젝트 02 - 파이썬 기반 데이터 활용

## 후기

 ### 1. 코드 및 해설



#### 00. API 문서와 requests 활용(연습)

> API 사이트로 원하는 데이터 가져와서 출력하기

```python
# API 문서와 requests 활용(연습)
# BTC(비트코인)의 KRW(원) 전일종가 출력

import requests
# URL 생성
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)
# 응답 받은 값을 가져옵니다.
# print(response)

# .json() 메서드는 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경합니다.
# print(response.json())

data = response.json()

print(data.get('data').get('prev_closing_price'))

```



#### 01. 인기 영화 조회

> api_key를 발급 받아 원하는 데이터를 요청하여 출력하기 

```python
import os
from dotenv import load_dotenv
import requests


load_dotenv()

# 인기 영화 목록의 개수 출력
# 현재 인기 있는 영화 목록(Get Populations)에 데이터를 요청

def popular_count():
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR'        
    }
    
    response = requests.get(BASE_URL+path, params=params).json()
    # /movie/popular에 있는 값 json으로 불러와서 response 에 저장합니다.
    # print(response.keys())
    # response의 key 목록 확인
    # print(type(response['results'])) # <class 'list'>
    cnt = 0
    for n in response['results']:
        n.get('id')
        cnt += 1
    # print(cnt)
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
```



#### 02. 특정 조건에 맞는 인기 영화 조회

> 데이터를 가져와서 활용하여 원하는 값을 반환하는 함수를 작성하기

```python
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력
# 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청
# 평점(vote_average)이 8점 이상인 영화 목록을 리스트로 반환

def vote_average_movies():
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR'        
    }
    
    response = requests.get(BASE_URL+path, params=params).json()
    # print(response)
    # response의 타입은 딕셔너리
    result_list = response['results']
    # 딕셔너리이므로 'results'키 값으로 접근합니다.
    # print(type(result_list) # <class 'list'>
    # result_list의 타입은 list
    choice_movie = []
    for dict in result_list:
          # 리스트 result를 순회하면서
          if int(dict['vote_average']) >= 8:
            # 'vote_average' 키의 값이 8이상이면, (평점이 8점 이상이면) 
            # 값이 문자열일수도 있으니 int 형 변환
                choice_movie += [dict]
                # 해당 딕셔너리를 choice_movie 리스트에 추가합니다.(리스트에 추가)
    return choice_movie
    # 8점 이상 영화가 모인 리스트를 반환합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """
```



#### 03.  특정 조건에 맞는 인기 영화 조회

> sorted() 함수를 활용하여 키의 '값'을 기준으로 정렬하기

```python
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# 인기 영화 목록을 평점이 높은 순으로 5개 정렬하는 데이터 목록을 반환
# 영화 목록(Get Populations) 데이터를 요청하여 
# 평점이 높은 영화 5개의 정보를 리스트로 반환하는 함수 작성

def ranking():
      
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR'        
    }
    
    response = requests.get(BASE_URL+path, params=params).json()
    # 요청을 해서 response를 받아옵니다. response는 딕셔너리
    result_list = response['results']
    # 딕셔너리에서 'results' 키의 값으로 리스트를 가져오고 result_list에 할당합니다.
    sort_list = (sorted(result_list, key = lambda x:-x.get('vote_average')))
    # sorted() 의 key를 통해 정렬할 기준을 정합니다.
    # result_list의 요소는 딕셔너리이므로 'vote_average'의 키 값을 반환하는 
    # lambda 함수를 지정합니다.
    # sorted()의 key는 해당 함수를 기준으로 하므로 'vote_average'를 기준으로 오름차순으로 요소를 정렬합니다.
    # 높은 순이므로 내림차순 정렬을 위해 마이너스(-)를 추가합니다.
    rank_movie = sort_list[:5]
    # 내림차순 5개 영화 정렬이므로 해당 리스트를 인덱스로 접근합니다.
    return(rank_movie)
          
          
         

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """

```



#### 04. 영화 조회 및 추천 영화 조회

> requests로 받은 데이터를 활용하여 API의 다른 값도 요청하기

```PYTHON
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# 영화 제목으로 검색을 하여 추천 영화 목록을 출력
# TMDB에서 영화제목으로 영화를 검색(Search Movies)
# 추천 영화 목록을 리스트로 반환하는 함수 작성

def recommendation(title):
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR',
        'query' : title      
    }
        
    response = requests.get(BASE_URL + path, params=params).json().get('results')
    if len(response) == 0:
        return 
    # response에 값이 없다면 None을 반환하며 함수 종료합니다.
    # response의 타입은 딕셔너리가 아닌 리스트
    
    path_recommend = f'/movie/{response[0].get("id")}/recommendations'
    # response[0] 번째 인덱스에 접근하면 첫 번째 영화 정보의 딕셔너리이므로 
    # .get 함수로 'id'의 값을 가져옵니다.
    
    # 요청하는 값이 달라지므로 params의 값도 재설정합니다.
    params_2 = {
        'api_key': 'e0c0d3622b43ae47c6135b0a8f2cb8f2',
        'language' : 'ko-KR'        
    }
    
    # 값을 요청해서 받아옵니다.
    response = requests.get(BASE_URL + path_recommend, params=params_2).json().get('results')
    recommend_list = []
    for t in response:
        recommend_list += [t.get('title')]
        # 추천 영화 목록에 'title'키의 값을 추가합니다.
    return recommend_list
    

        
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

```



#### 05. 출연진 및 연출진 데이터 조회

> 같은 딕셔너리 내에 서로 다른 데이터를 요청해서 받아오기

```python
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# 영화 제목으로 검색을 하여 해당 영화의 출연진(cast) 그리고 스태프(crew) 중 '연출진'으로 구성된 목록만을 출력
# requests 라이브러리로 영화제목으로 검색
# 응답 받은 결과 중 첫 번째 영화의 id값을 활용하여 해당 영화에 대한 출연진과 스태프(cast and crew) 목록을 가져옴
# 출연진 중 cast_id 값이 10미만인 출연진만 추출하고,
# 연출진은 부서(department)가 directing인 데이터만 추출
# cast와 directing으로 구성된 딕셔너리에 추출된 값을 '리스트'에 출력하는 함수 작성

def credits(title):
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'e0c0d3622b43ae47c6135b0a8f2cb8f2',
        'language' : 'ko-KR',
        'query' : title      
    }
        
    response = requests.get(BASE_URL + path, params=params).json().get('results')
    # json()으로 변환한 값= 딕셔너리에서 'result' 키의 값= 리스트 을 response에 할당합니다.
    if len(response) == 0:
        return 
    # 키의 값이 없다면(검색한 영화가 없을 경우) 함수를 종료하며 None 을 반환합니다.
    path_credits = f'/movie/{response[0].get("id")}/credits'
    params_2 = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR'
    } 
    response_cast = requests.get(BASE_URL + path_credits, params = params_2).json().get('cast')
    # json()으로 변환한 값 = 딕셔너리에서 'cast'키의 값= 리스트를 response_cast에 할당합니다.
    # 'cast'리스트 안에 있는 딕셔너리의 'cast_id'의 키값에 접근합니다.
    response_crew = requests.get(BASE_URL + path_credits, params = params_2).json().get('crew')
    # 'crew' 리스트 안에 있는 딕셔너리의 'department'의 키값에 접근합니다.
    
    # cast_id 의 값이 10 미만인 출연진들의 이름 리스트
    cast_list = []
    # crew_list 의 값이 Directing인 연출진들의 이름 리스트
    crew_list = []
    credit_info = {"cast" : cast_list  , "crew" : crew_list }
    # 각각의 리스트를 딕셔너리의 값으로 추가합니다.
    for cast in response_cast:
        if cast.get('cast_id') < 10:
            credit_info["cast"] += [cast.get('name')]
            # cast_list 는 리스트의 형태이므로 리스트 추가 형태로 추가합니다.
    for crew in response_crew:
        if crew.get('department') == 'Directing':
            credit_info["crew"] += [crew.get('name')]
            # crew_list 역시 마찬가지
   
    return credit_info
    # {cast : 값 , crew: 값}의 형태를 가진 딕셔너리를 반환합니다.
    
        
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

```



### 2. 배운 점, 느낀 점



**1.  API는 주어진대로만 하면 되는구나.📜**

     이번 프로젝트가 지난 번보다 쉽게 느껴진 이유는 양식이 이미 API 사이트에 다 제시되어 있고, 강사님이 수업 시간에 다뤄주신 부분에서 크게 다르지 않았기 때문이라고 생각한다. 원하는 데이터를 출력하기 위해 어떤 url을 추가해야 하는지 찾는 것도 API라는 시스템이 낯설었기 때문이지, 어려운 일은 아닌 것 같았다.



**2. 익숙해지는 것이 최고의 성과 💪**

     또한 이번 프로젝트가 비교적 수월했던 것도, 문제 배치의 적절함 덕분이다. 00.(연습)문제를 통해 API에서 데이터를 가져오는 것을 연습하고, api_key를 발급받아 데이터를 요청하고 받아오는 데 익숙해졌다.
    03.sort()의 key를 활용하는 문제를 통해 lambda를 한 번이라도 더 활용해 볼 수 있었고, 그 이후 받아온 데이터들을 원하는 데이터만 추출 및 출력하도록 단계적으로 문제의 요구사항이 추가되면서 API는 이전의 반복문처럼 친숙해질 수 있었다. 그리고 그것이 이번 프로젝트의 최고 성과라고 생각한다.



**3. 하지만 나를 잊지말아주석. 😭**

    당연히 물론 기본적인 단계임에 불과하겠지만 API에서 데이터를 불러오는 것이 익숙해지면서 처음엔 한 줄 한 줄 적어나가던 주석도 어느샌가 차츰 뛰어 넘어버리고 다음 코드를 작성하고 있는 모습을 발견할 수 있었다. 
    분명 좋은 일이지만, 아직 습관도 채 다져지지 않은 초급생한테는 경계해야 일이라고 생각한다. 주석은 내가 어떤 코드를 작성하고 있었는지, 어떤 접근을 하고 있었는지 알려주는 고마운 친구다. 늘, 초심을 잊지 말 것.



두 번째 프로젝트를 마지막으로 파이썬 과목 강의는 정식적으로 끝이 났다.

그런데 벌써부터 기억이 가물가물하다. 밥 먹듯이 반복문을 쓰고 있지만, 그래서 그런지 함수에 대한 개념이 약하다. 파이썬 code_up 문제풀이도 다 못 끝냈고 말이다.

파이썬 강의는 끝났지만, 개념이 약하다보니 Notion - 자료공유 탭은 화면에서 사라질 일이 없을 거 같다.

다음 시간부터는 알고리즘 문제 풀이를 본격적으로 하게 되는데, 걱정이 앞선다. 하지만 첫 번째 프로젝트 이후 딕셔너리가 친숙해졌고, 두 번째 프로젝트 이후 API가 친숙해진 것처럼 알고리즘과도 시간 끝에 풀 수 있다는 자신감과 친숙함이 찾아오기를 기대한다.

그리고 이제 다른 수강생의 코드 리뷰를 본격적으로 진행해봐야 할 것 같다. 지금까지는 코드를 작성하는 것 자체도 어렵게 느껴졌고, 코드를 봐도 이해하는 데 급급했다. 04.의 문제는 다른 코드를 참고해서 풀었는데, 접근 방법이 같으니 코드를 이해하는 게 한결 쉽게 느껴졌다. '비교'라는 게 가능해진 시점이 되니 어제보다는 나은 사람이 되었구나,가 느껴지는 부분이었다. 

그러다보니 해결하는 거로만 그치기보다는 근본적으로 정리하고 학습해야겠단 생각이 들었다. 하루 한 문제라도 미처 생각 못한 부분을 발견하고 다음부터는 어떻게 고칠지 고민해보는 코드 리뷰 시간을 가져야겠다는 결심을 들게 하는 두 번째 개인 프로젝트였다.
