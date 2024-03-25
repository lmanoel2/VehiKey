class BaseException(Exception):
    def __init__(self, message="Generic Exception"):
        self.message = message
        super().__init__(self.message)


class EntityNotFoundException(BaseException):
    def __init__(self, message="Entity not found"):
        self.message = message
        super().__init__(self.message)

class ValidTimeNotFormattedError(BaseException):
    def __init__(self, message="Valid time is not formatted correctly 'dd-mm-yyyy-hh-mm dd-mm-yyyy-hh-mm'"):
        self.message = message
        super().__init__(self.message)