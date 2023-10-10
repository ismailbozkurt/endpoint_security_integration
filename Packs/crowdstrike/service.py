from core.integration import BaseProduct


class Service(BaseProduct):
    def integrate(self, keys):
        return True

    def deintegrate(self):
        pass

    def add_ip(self, ip):
        pass

    def remove_ip(self, ip):
        pass
