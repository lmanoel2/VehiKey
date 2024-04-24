from pydantic import BaseModel
from typing import Optional


class PubSubRequestView(BaseModel):
    action: str
    topic_suffix: str
