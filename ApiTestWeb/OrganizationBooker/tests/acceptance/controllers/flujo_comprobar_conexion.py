from behave import *
from consts import URL_BASE
from servicios.factory_conexion import RequestFactory
from Logs import logs_test

log = logs_test.get_logs()

class flujoComprobarConexion(RequestFactory):
        
    url = f'{URL_BASE}/ping'
    
    headers = {'content-type': 'application/json'}

    def send_request_ping_api(self):
        self.resp_ping = self.build_request(type_req="request_get").request_type(self.url, self.headers)

    def response_ping(context):
        log.info(f'La respuesta a la conexion es -> {context.resp_ping.status_code}')
        assert context.resp_ping.status_code == 201
