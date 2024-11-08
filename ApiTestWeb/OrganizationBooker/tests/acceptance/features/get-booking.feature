Feature: Probando funcionalidad de API Restful-booker 

  Scenario: Obtener clientes
    Given Realizo la peticion a la api
     Then Recibo respuesta de objeto json con los clientes

  Scenario Outline: Obtener Clientes Falla
     Given Realizo la peticion con ruta: <route> errada
      Then Respuesta fallida al obtener clientes

      Examples: 
            |route|
            |clientes| 
            |123546312|
            