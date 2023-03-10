from pydantic import BaseModel

class Token(BaseModel):
    id: int
    token: str
    user_id: int

    def __str__(self):
        return f"{self.token}"