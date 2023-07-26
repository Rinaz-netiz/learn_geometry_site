from typing import List, Iterable, Dict


class Pagination:
    def __init__(self, iterable: Iterable, on_page: int, page: str = 1) -> None:
        self.iterable = iterable
        self.on_page = on_page
        self._now_page = int(page)
        
    def pages(self):
        lst = []
        for num in range(2, self.length()):
            lst.append({"num": num, "url": f"?page={num}"})
            
        return lst
    
    def length(self) -> int:
        return len(self.iterable)//self.on_page
    
    def first_page(self) -> str:
        return "?page=1"
    
    def last_page(self) -> str:
        return f"?page={self.length()}"
    
    def get_content(self) -> List:
        start = (self._now_page - 1)*self.on_page
        end = (self._now_page * self.on_page) 
        return self.iterable[start:end]
    
    
    