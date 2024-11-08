from behave import *
from consts import URL_BASE
from servicios.factory_conexion import RequestFactory
from Logs import logs_test

log = logs_test.get_logs()

class FlujoObtenerBooking(RequestFactory):
        
    url = f'{URL_BASE}/booking'
    body = {}
    headers = {'content-type': 'application/json'}

    def request_api(self):
        self.res = self.build_request(type_req="request_get").request_type(self.url, self.headers)
        
    def response_api(self):
        log.info(f'El status de la respuesta al obtener clientes es:-> {self.res.status_code}')
        
        arr_res = self.res.json()[0]
           
        assert self.search_value_in(arr_res, "bookingid")
        assert self.res.json()
        assert self.res.ok
        assert self.res.status_code == 200
   

    def request_api_route_error(self, route):
        url_errada = f"{URL_BASE}/{route}"
        self.res_err = self.build_request(type_req="request_get").request_type(url_errada, self.headers)

    def response_api_fallida(self):
        log.error(f'El status de la respuesta al obtener clientes es:-> {self.res_err.status_code} ')
        assert self.res_err.status_code == 404


    def search_value_in(self, arrDeObject, value):
        if len(arrDeObject) > 0 :
            if value in arrDeObject.keys():
                return True
            else:
                return False