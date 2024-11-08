from behave import *
from Logs import logs_test

log = logs_test.get_logs()

@given('Envio mi Username: {username} y mi password: {password}')
def set_impl(context, username, password):
    context.app.flujoObtenerToken.send_username_password(username, password)

@when('Realizo la peticion a la api')
def step_impl(context):
   context.app.flujoObtenerToken.request_api()

@then('Recibo respuesta de objeto json con el token')
def step_impl(context):
    context.app.flujoObtenerToken.response_api()
