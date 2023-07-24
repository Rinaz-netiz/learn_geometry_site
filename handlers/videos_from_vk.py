import requests

from config.config import config


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


def get_videos():
    """Получение видео"""
    return pars_data(request(config.vk_token))

