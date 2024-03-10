from Infra.Controllers.BaseController import BaseController


class CRUDController(BaseController):
    @staticmethod
    def Create():
        raise NotImplementedError()

    @staticmethod
    def Get():
        raise NotImplementedError()

    @staticmethod
    def Update():
        raise NotImplementedError()

    @staticmethod
    def Delete():
        raise NotImplementedError()