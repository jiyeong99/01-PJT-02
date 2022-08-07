import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params={
        'api_key':'9e7ad8abf0f44312c8921229635fe29f',
        'language':'ko-KR'
    }
    Response = requests.get(Base_URL+path, params=params).json()
    movies=len(Response.get('results'))
    return movies
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
