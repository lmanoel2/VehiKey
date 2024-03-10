class PlateAlreadyExistsError(Exception):
    def __init__(self, message="Duplicate license plate"):
        self.message = message
        super().__init__(self.message)
