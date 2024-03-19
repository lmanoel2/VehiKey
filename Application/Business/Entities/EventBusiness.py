from Application.Business.Entities.CRUDBusiness import CRUDBusiness
from Domain.Entities.Event import Event


class EventBusiness(CRUDBusiness):
    def __init__(self):
        super().__init__(Event)

    def Create(self, model: Event):
        super().Create(model)
