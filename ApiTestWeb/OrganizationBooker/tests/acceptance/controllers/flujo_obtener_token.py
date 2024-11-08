from behave import *
from servicios.singleton_entorno import Entorno
from consts import URL_BASE
from servicios.factory_conexion import RequestFactory
from Logs import logs_test

log = logs_test.get_logs()

class FlujoObtenerToken(RequestFactory):
        
    url = f'{URL_BASE}/auth'
    body = {}
    headers = {'content-type': 'application/json'}
    
    def send_username_password(self, username, password):
        self.body['username'] = username
        self.body['password'] = password   
    def request_api(self):
        entorno = Entorno()
        self.res = self.build_request(type_req="request_post").request_type(self.url, self.body, self.headers)
      
        log.info(self.res.json()['token'])
        

        entorno.set_token(self.res.json()['token'])

    def response_api(self):
        log.info(f'La respuesta al pedido del token es -> {self.res.status_code}')
        
        assert self.res.status_code == 200
        assert self.res.json()['token'] 
    