class IpAlreadyExistsError(BaseException):
    def __init__(self, message="Duplicate ip"):
        self.message = message
        super().__init__(self.message)
