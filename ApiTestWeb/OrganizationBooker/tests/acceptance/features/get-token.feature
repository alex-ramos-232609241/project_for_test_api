Feature: Probando funcionalidad de API Restful-booker 
  Scenario Outline: Obtener token para Authorizacion
    Given Envio mi Username: <username> y mi password: <password>
     When Realizo la peticion a la api
     Then Recibo respuesta de objeto json con el token

    Examples: Credenciales  
      | username  | password     |
      | admin     | password123  |
