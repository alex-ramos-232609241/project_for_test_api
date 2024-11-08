from behave import *
from Logs import logs_test

log = logs_test.get_logs()


@given('Realizo la peticion a la api')
def step_impl(context):
   context.app.flujoObtenerBooking.request_api()

@then('Recibo respuesta de objeto json con los clientes')
def step_impl(context):
    context.app.flujoObtenerBooking.response_api()
 

@given('Realizo la peticion con ruta: {route} errada')
def step_impl(context, route):
   context.app.flujoObtenerBooking.request_api_route_error(route)

@then('Respuesta fallida al obtener clientes')
def step_impl(context):
    context.app.flujoObtenerBooking.response_api_fallida()
 