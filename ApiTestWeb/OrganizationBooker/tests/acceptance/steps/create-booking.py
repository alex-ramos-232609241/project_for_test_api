from behave import *
from Logs import logs_test

log = logs_test.get_logs()


@given('Enviando datos y realizando peticion con {firstname} {lastname}')
def step_impl(context, firstname, lastname):
   context.app.flujoCrearBooking.request_api_create(firstname, lastname)

@given('Datos tambien a enviar {totalprice} {depositpaid} {checkin} {checkout} {additionalneeds}')
def step_impl(context, totalprice, depositpaid, checkin, checkout, additionalneeds):
   context.app.flujoCrearBooking.request_api_create_data_full(totalprice, depositpaid, checkin, checkout, additionalneeds)

@then('Respuesta al crear booking valido')
def step_impl(context):
   context.app.flujoCrearBooking.response_api_create()



@given('Realizo la peticion con algunos datos invalidos {firstname} {lastname}')
def step_impl(context, firstname, lastname):
    context.app.flujoCrearBooking.request_api_create_error(firstname, lastname)

@given('Datos con error a enviar {totalprice} {depositpaid} {checkin} {checkout} {additionalneeds}')
def step_impl(context, totalprice, depositpaid, checkin, checkout, additionalneeds):
   context.app.flujoCrearBooking.request_api_create_data_full_error(totalprice, depositpaid, checkin, checkout, additionalneeds)

@then('Respuesta Fallida al crear booking')
def step_impl(context):
    context.app.flujoCrearBooking.response_api_create_error()
 
