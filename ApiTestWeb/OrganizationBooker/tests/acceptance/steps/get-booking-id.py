from behave import *
from Logs import logs_test

log = logs_test.get_logs()


@given('Realizo la peticion con id: {id} valido')
def step_impl(context, id):
   context.app.flujoObtenerBookingId.request_api_id(id)

@then('Respuesta al obtener cliente')
def step_impl(context):
    context.app.flujoObtenerBookingId.response_api_id()
 

@given('Realizo la peticion con id: {id} errada')
def step_impl(context, id):
   context.app.flujoObtenerBookingId.request_api_id_error(id)

@then('Respuesta Fallida al obtener cliente')
def step_impl(context):
    context.app.flujoObtenerBookingId.response_api_id_fallida()
 