import requests


def request(token: str) -> dict:
    """Запрос в вк"""
    return requests.get("https://api.vk.com/method/video.get", 
                 params={
                     'access_token': token,
                     'v': "5.131",
                     "owner_id": "-165635569",
                 }).json()
    
    
def pars_data(response: dict) -> list:
    """Парсинг данных"""
    try:
        data = response["response"]["items"]
    except KeyError:
        return []

    videos = []
    for video in data:
        videos.append({
            "image": video["image"][-1],
            "player": video["player"],
            "title": video["title"]
        })
        
    return videos


def get_videos(token):
    """Получение видео"""
    return pars_data(request(token))


if __name__ == "__main__":
    get_videos("vk1.a.DtYYSIGRFQT00dGDRoPXTJGS2UL6S0KxNmM_FZNiJ9S__YhGM57ZCNznYj9CpoW-UGjQ0OmyVEXY2NOfPnE04oZT94jT3DCxgTCWtP3VzgJGtVJl9L3VKxn9XU61PMnvKpN3fqsfQ4ocB2dzjhoaT6jrrNj-0qWke65bM5yZfC34cfZz0g8EQIOd3HSQvQFRYnFkxk9YxQcXFPF7t8s8QQ")
