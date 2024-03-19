from pydantic import BaseModel


class EventModel(BaseModel):
    message: str
