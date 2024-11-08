from behave import *
from consts import URL_BASE
from servicios.factory_conexion import RequestFactory
from Logs import logs_test

log = logs_test.get_logs()

class FlujoObtenerBookingId(RequestFactory):
        
    url = f'{URL_BASE}/booking'
    body = {}
    headers = {'content-type': 'application/json'}

    def request_api_id(self, id):
        self.res_id = self.build_request(type_req="request_get").request_type(f'{self.url}/{id}', self.headers)
        print('*****Response id*****')
        print(self.res_id)
        print('----------------')
    def response_api_id(self):
        log.info(f'El status de la respuesta al obtener el cliente es:-> {self.res_id.status_code}')
        
        json_res_id = self.res_id.json()
        
        struct_example = {
                "firstname": "Jim",
                "lastname": "Jones",
                "totalprice": 186,
                "depositpaid": 'true',
                "bookingdates": {
                    "checkin": "2020-03-16",
                    "checkout": "2022-07-26"
                }
            }
        self.search_struct(json_res_id, struct_example)
        assert self.res_id.json()
        assert self.res_id.ok
        assert self.res_id.status_code == 200

    def request_api_id_error(self, id):
        self.res_id_error = self.build_request(type_req="request_get").request_type(f'{self.url}/{id}', self.headers)


    def response_api_id_fallida(self):
        log.error(f'El status de la respuesta al obtener clientes por id es:-> {self.res_id_error.status_code} ')
        assert self.res_id_error.status_code == 404 

    def search_struct(self, j_res_id, s_example):
        arr_keys_valid = [*s_example]
        arr_keys_probar = [*j_res_id]

        assert arr_keys_valid[0] == arr_keys_probar[0]
        assert arr_keys_valid[1] == arr_keys_probar[1]
        assert arr_keys_valid[2] == arr_keys_probar[2]
        assert arr_keys_valid[3] == arr_keys_probar[3]
