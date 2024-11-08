from abc import ABC, abstractmethod
import json
import requests

class AbstractRequest(ABC):
    
    @abstractmethod
    def request_type(self, *args):
        pass

class RequestGet(AbstractRequest):
        
    def request_type(self, url, headers):
        return requests.get(url, headers)
    
class RequestPost(AbstractRequest):
    
    def request_type(self, url, body, headers):
        return requests.post(url, data=json.dumps(body), headers=headers)
    
class RequestPut(AbstractRequest):
    
    def request_type(self, url, body, headers):
        return requests.put(url, data=json.dumps(body), headers=headers)

class RequestPatch(AbstractRequest):
    
    def request_type(self, url, body, headers):
        return requests.patch(url, data=body, headers=headers )

class RequestDelete(AbstractRequest):
    
    def request_type(self, url, body, headers):
        return requests.delete(url, data=json.dumps(body), headers=headers)
      
class RequestFactory():
    
    @staticmethod
    def build_request(type_req):
        try:
            if type_req == "request_get":
                return RequestGet()
            elif type_req == "request_post":
                return RequestPost()
            elif type_req == "request_put":
                return RequestPut()
            elif type_req == "request_patch":
                return RequestPatch()
            elif type_req == "request_delete":
                return RequestDelete()    
            raise AssertionError("Error no es un tipo de peticion valida.")
        except AssertionError as e:
            print(e)