import json
from behave import *
from consts import URL_BASE
from servicios.factory_conexion import RequestFactory
from Logs import logs_test

log = logs_test.get_logs()

class FlujoCrearBooking(RequestFactory):
        
    url = f'{URL_BASE}/booking'
    body = { }
    headers = {'content-type': 'application/json'}

    struct_valid_response = {
            "bookingid": 4046,
            "booking": {
                "firstname": "Jim",
                "lastname": "Brown",
                "totalprice": 111,
                "depositpaid": 'true',
                "bookingdates": {
                    "checkin": "2018-01-01",
                    "checkout": "2019-01-01"
                },
                "additionalneeds": "Breakfast"
            }
        }   

    def request_api_create(self, firstname, lastname): 
        self.body['firstname'] = firstname
        self.body['lastname'] = lastname

    def request_api_create_data_full(self, totalprice, depositpaid, checkin, checkout, additionalneeds):    
        self.body['totalprice'] = int(totalprice)
        self.body['depositpaid'] = depositpaid
        bookingdates = {"checkin": checkin,
                        "checkout": checkout}
        self.body['bookingdates'] = bookingdates
        self.body['additionalneeds'] = additionalneeds
        self.res_create = self.build_request(type_req="request_post").request_type(self.url, self.body ,self.headers)


    def response_api_create(self):
        log.info(f'El status de la respuesta al crear booking:-> {self.res_create.status_code} ')
        
        json_response = self.res_create.json()

        self.validate_struct_response(json_response, self.struct_valid_response)
        assert self.res_create.json()
        assert self.res_create.ok
        assert self.res_create.status_code == 200


    
    def request_api_create_error(self, firstname, lastname): 
        self.body['firstname'] = firstname
        self.body['lastname'] = lastname

    def request_api_create_data_full_error(self, totalprice, depositpaid, checkin, checkout, additionalneeds):    
        self.body['totalprice'] = totalprice
        self.body['depositpaid'] = depositpaid
        bookingdates = {"checkin": checkin,
                        "checkout": checkout}
        self.body['bookingdates'] = bookingdates
        self.body['additionalneeds'] = additionalneeds
        self.res_create_error = self.build_request(type_req="request_post").request_type(self.url, self.body ,self.headers)


    def response_api_create_error(self):
        log.info(f'El status de la respuesta al crear booking con error:-> {self.res_create_error.status_code} ')
        
        assert self.res_create_error.status_code == 200 #te esta dejando crear con cualquier nombre y datos invalidos


    def validate_struct_response(self, json_response, struct_valid_response):
        json_response = [*json_response]
        arr_keys_json_response = [*struct_valid_response]

        assert json_response[0] == arr_keys_json_response[0]
        assert json_response[1] == arr_keys_json_response[1]
        
