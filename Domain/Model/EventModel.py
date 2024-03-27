from pydantic import BaseModel


class EventModel(BaseModel):
    message: str
    sent_to_server: bool
