Feature: Probando funcionalidad de API Restful-booker 

  Scenario Outline: Update booking con exito
      Given Obteniendo token
      Given Enviando datos para actualizar booking <firstname> <lastname>
      Given Tambien envio estos datos <id> <totalprice> <depositpaid> <checkin> <checkout> <additionalneeds>
      Then Respuesta al Actualizar booking valido

      Examples: 
        |  id| firstname | lastname | totalprice   |  depositpaid  | checkin    | checkout   |additionalneeds|
        |   1744| Jimex       | Brownie    | 111          |  true         | 2018-01-01 | 2019-01-01 |  Breakfast    |
        |    484| alan      | turing   | 500          |  true         | 2020-02-04 | 2020-02-10 |  Breakfast    |
            
