Feature: Probando funcionalidad de API Restful-booker 

  Scenario Outline: Obtener Cliente por id valido
     Given Realizo la peticion con id: <id> valido
      Then Respuesta al obtener cliente

      Examples: 
            |  id   |
            |  424 | 
            |  477  |

  Scenario Outline: Obtener Cliente por id invalido
     Given Realizo la peticion con id: <id> errada
      Then Respuesta Fallida al obtener cliente

      Examples: 
            |  id   |
            |  985488555 | 
            |  123456789 |
            