from behave import *
from Logs import logs_test

log = logs_test.get_logs()

@given('Consulto la conexion a la api')
def set_impl(context):
    context.app.flujoComprobarConexion.send_request_ping_api()

@then('Recibo una respuesta status correcto')
def response_ping(context):
    context.app.flujoComprobarConexion.response_ping()
