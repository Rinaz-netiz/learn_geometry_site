import sqlite3 as sq
from typing import List, Tuple, Callable, Optional, NoReturn


class SQL:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        
        self.create_table_in_db()


    def connect(func: Callable) -> Callable:
        def wrapped(self, *args, **kwargs):
            try:
                con = sq.connect(f"{self.db_name}")
                kwargs["cursor"] = con.cursor()
                kwargs["con"] = con
                return func(self, *args, **kwargs)
            finally:
                con.close()
        return wrapped


    @connect
    def create_table_in_db(self, *args, **kwargs) -> None:
        kwargs["cursor"].execute(f"""CREATE TABLE IF NOT EXISTS {self.table_name}(
                        url TEXT, 
                        ready BLOB
                        )""") 
    
    @connect
    def insert_data_to_db(self, data: Tuple, *args, **kwargs) -> Optional[NoReturn]:
        try:
            kwargs["cursor"].execute(f"""
                                        INSERT INTO {self.table_name} (url, ready)
                                        VALUES (?,?)
                                    """, data)
            kwargs["con"].commit()
        except sq.OperationalError:
            raise ValueError("Table is none")
    
    @connect
    def select_all(self, *args, **kwargs) -> List | NoReturn:
        try:
            kwargs["cursor"].execute(f"""SELECT * FROM {self.table_name}""")
        except sq.OperationalError:
            raise ValueError("Table is none")
        
        return kwargs["cursor"].fetchall()
        
    @connect
    def update_data(self, data: Tuple, *args, **kwargs) -> Optional[NoReturn]:
        try:
            kwargs["cursor"].execute(f"""
                                        UPDATE {self.table_name} 
                                        SET ready = ?
                                        WHERE url = ?
                                    """, data)
            kwargs["con"].commit()
        except sq.OperationalError:
            raise ValueError("Table is none")
        
    @connect
    def bunch_insert(self, data: List[Tuple], *args, **kwargs) -> Optional[NoReturn]:
        try:
            kwargs["cursor"].executemany(f"""
                                        INSERT INTO {self.table_name} (url, ready)
                                        VALUES (?,?)
                                    """, data)
            kwargs["con"].commit()
        except sq.OperationalError:
            raise ValueError("Table is none")
    

if __name__ == "__main__":
    sql = SQL("vk_videos.db", "videos")
