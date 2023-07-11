import requests
from typing import Optional


def request(token: str) -> dict:
    """Запрос в вк"""
    return requests.get("https://api.vk.com/method/video.get", 
                 params={
                     'access_token': token,
                     'v': "5.131",
                     "owner_id": "-165635569",
                 }).json()
    
    
def pars_data(response: dict) -> Optional[list[dict]]:
    """Парсинг данных"""
    try:
        data = response["response"]["items"]
    except KeyError:
        return

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
    get_videos()
