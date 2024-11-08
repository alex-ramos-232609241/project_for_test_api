from behave import *
from servicios.singleton_entorno import Entorno
from consts import URL_BASE
from servicios.factory_conexion import RequestFactory
from Logs import logs_test

log = logs_test.get_logs()

class FlujoActualizarBooking(RequestFactory):
    
    
    url = f'{URL_BASE}/booking'
    body = { }
    
    headers = {}
    def get_token_entorno(self):
        entorno = Entorno()
        token = entorno.get_token()
        print('----*TOKEN*----')
        print(token)
        print('-------------')
        self.headers = {'content-type': 'application/json', 'Cookie':f'token={token}'}

    def request_api_actualizar(self, firstname, lastname): 
        self.body['firstname'] = firstname
        self.body['lastname'] = lastname

    def request_api_actualizar_data_full(self, id, totalprice, depositpaid, checkin, checkout, additionalneeds):    
        self.body['totalprice'] = int(totalprice)
        self.body['depositpaid'] = depositpaid
        bookingdates = {"checkin": checkin,
                        "checkout": checkout}
        self.body['bookingdates'] = bookingdates
        self.body['additionalneeds'] = additionalneeds
        print('******HEADERS******')
        print(self.headers)
        print('*******************')
        self.res_update = self.build_request(type_req="request_put").request_type(f"{self.url}/{id}", self.body ,self.headers)


    def response_api_actualizar(self):
        log.info(f'El status de la respuesta al actualizar booking:-> {self.res_update.status_code} ')
        
        assert self.res_update.json()
        assert self.res_update.ok
        assert self.res_update.status_code == 200
