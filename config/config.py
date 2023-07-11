from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()


@dataclass
class Config:
    vk_token: str
    

config = Config(
    vk_token="vk1.a.DtYYSIGRFQT00dGDRoPXTJGS2UL6S0KxNmM_FZNiJ9S__YhGM57ZCNznYj9CpoW-UGjQ0OmyVEXY2NOfPnE04oZT94jT3DCxgTCWtP3VzgJGtVJl9L3VKxn9XU61PMnvKpN3fqsfQ4ocB2dzjhoaT6jrrNj-0qWke65bM5yZfC34cfZz0g8EQIOd3HSQvQFRYnFkxk9YxQcXFPF7t8s8QQ"
    # vk_token=os.getenv("ACCESS_TOKEN")
)


