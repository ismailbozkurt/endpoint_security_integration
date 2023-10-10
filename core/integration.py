from core.base_product import BaseProduct


class IntegrationService():
    __services = dict()

    @classmethod
    def add_service(cls, name, module):
        cls.__services.setdefault(name, module)

    @classmethod
    def get_service(cls, name) -> BaseProduct:
        return cls.__services.get(name, None)

    @classmethod
    def remove_service(cls, name):
        if name in cls.__services:
            cls.__services.pop(name)
