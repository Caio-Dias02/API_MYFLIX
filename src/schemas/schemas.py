from typing import Optional
from pydantic import BaseModel

class Serie(BaseModel):
    id: Optional[int] = None
    title: str
    year: int
    gender: str
    seasons: str

    class Config: 
        orm_mode = True

        