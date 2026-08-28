from pydantic import BaseModel

class JobTitleInfo(BaseModel):
    id: int
    name: str
    