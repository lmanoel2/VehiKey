class CameraResponseView:
    id: int
    ip: str
    port: int
    password: str
    user: str
    name: str
    manufacturer: str
    valid_time: str
    controller: str

    def __init__(self, id: int, ip: str, port: str, password: str, user: str, name: str, manufacturer: str, valid_time: str = None, controller: str = None):
        self.id = id
        self.ip = ip
        self.port = port
        self.password = password
        self.user = user
        self.name = name
        self.manufacturer = manufacturer
        self.valid_time = valid_time
        self.controller = controller
