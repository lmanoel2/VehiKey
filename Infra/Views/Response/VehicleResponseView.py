class VehicleResponseView:
    id: int
    color: str
    plate: str

    def __init__(self, id: int, color: str, plate: str):
        self.id = id
        self.color = color
        self.plate = plate

