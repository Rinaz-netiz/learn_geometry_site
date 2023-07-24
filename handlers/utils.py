from typing import List, Dict, Optional

from db import sql
from .videos_from_vk import get_videos


def fill_db(data: List[Dict]) -> None:
    """Заполняет базу данных"""
    urls = []
    for i in data:
        urls.append((i["title"], False))
    
    sql.bunch_insert(urls)
    

def union_data() -> Optional[List[Dict]]:
    """Объединяет данные"""
    videos = get_videos()
    qs = sql.select_all()
    if not qs:
        fill_db(videos)
    
    if len(videos) != len(qs):
        return
    
    united: List[Dict] = []
    for video in videos:
        for query in qs:
            if video["title"] == query[0]:
                video["watched"] = query[1]
                united.append(video)
       
    return united
    