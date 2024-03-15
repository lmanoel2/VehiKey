class VehicleResponseView:
    id: int
    color: str
    plate: str
    valid_time: str
    access_time: str
    number_access: int

    def __init__(self, id: int, color: str, plate: str, valid_time: str = None, access_time: str = None, number_access: int = None):
        self.id = id
        self.color = color
        self.plate = plate
        self.valid_time = valid_time
        self.access_time = access_time
        self.number_access = number_access
