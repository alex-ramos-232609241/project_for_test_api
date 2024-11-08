from behave import *
from Logs import logs_test

log = logs_test.get_logs()

@given('Obteniendo token')
def set_impl(context):
    context.app.flujoActualizarBooking.get_token_entorno()

@given('Enviando datos para actualizar booking {firstname} {lastname}')
def set_impl(context, firstname, lastname):
    context.app.flujoActualizarBooking.request_api_actualizar(firstname, lastname)

@given('Tambien envio estos datos {id} {totalprice} {depositpaid} {checkin} {checkout} {additionalneeds}')
def step_impl(context, id, totalprice, depositpaid, checkin, checkout, additionalneeds):
   context.app.flujoActualizarBooking.request_api_actualizar_data_full(id, totalprice, depositpaid, checkin, checkout, additionalneeds)

@then('Respuesta al Actualizar booking valido')
def step_impl(context):
    context.app.flujoActualizarBooking.response_api_actualizar()
