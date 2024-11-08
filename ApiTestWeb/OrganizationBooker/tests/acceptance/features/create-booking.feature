Feature: Probando funcionalidad de API Restful-booker 

  Scenario Outline: Create booking con exito
      Given Enviando datos y realizando peticion con <firstname> <lastname> 
      Given Datos tambien a enviar <totalprice> <depositpaid> <checkin> <checkout> <additionalneeds>
            """
                  {
                  "firstname" : "Jim",
                  "lastname" : "Brown",
                  "totalprice" : 111,
                  "depositpaid" : true,
                  "bookingdates" : {
                        "checkin" : "2018-01-01",
                        "checkout" : "2019-01-01"
                  },
                  "additionalneeds" : "Breakfast"
                  }
            """
      Then Respuesta al crear booking valido

      Examples: 
            | firstname | lastname | totalprice   |  depositpaid  | checkin    | checkout   |additionalneeds|
            | Jim       | Brown    | 111          |  true         | 2018-01-01 | 2019-01-01 |  Breakfast    |
            | alan      | turing   | 500          |  true         | 2020-02-04 | 2020-02-10 |  Breakfast    |
            

  Scenario Outline: Crear booking con error
      Given Realizo la peticion con algunos datos invalidos <firstname> <lastname> 
      Given Datos con error a enviar <totalprice> <depositpaid> <checkin> <checkout> <additionalneeds> 
      Then Respuesta Fallida al crear booking

      Examples: 
            | firstname | lastname | totalprice   |  depositpaid  | checkin    | checkout   |additionalneeds|
            | 12354     | Brown    | -111          |  true         | 2018-01-01 | 2019-01-01 |  Breakfast    |
            |  ##%???   | turing   | exit         |  true         | 2020-02-04 | 2020-02-10 |  Breakfast    |
            """
            OBS : para estos casos la api nos esta dejando crear 
            Existe mala implementacion.
            """
            