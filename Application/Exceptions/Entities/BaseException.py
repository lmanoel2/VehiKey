class BaseException(Exception):
    def __init__(self, message="Generic Exception"):
        self.message = message
        super().__init__(self.message)


class EntityNotFoundException(BaseException):
    def __init__(self, message="Entity not found"):
        self.message = message
        super().__init__(self.message)
