
class SinglentonEntorno(type):

    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instance = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instance
        return cls._instancias[cls]     

class Entorno(metaclass=SinglentonEntorno):
    
    token = ''

    def get_token(self):
        return self.token

    def set_token(self, value):
        self.token = value

