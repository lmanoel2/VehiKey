class MissingFieldsView:
    message: str
    def __init__(self, e):
        missingFields = str([error["loc"][0] for error in e.errors()])
        missingFields = missingFields.replace("'", '"')
        self.message = "Missing Fields " + str(missingFields)
