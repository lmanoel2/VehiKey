class ExceptionView:
    message: str
    def __init__(self, exception):
        self.message = str(exception)
