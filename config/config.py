from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()


@dataclass
class Config:
    vk_token: str
    

config = Config(
    vk_token=os.getenv("ACCESS_TOKEN")
)


