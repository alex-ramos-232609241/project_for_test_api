from controllers.flujo_crear_booking import FlujoCrearBooking
from controllers.flujo_obtener_token import FlujoObtenerToken
from controllers.flujo_obtener_booking import FlujoObtenerBooking
from controllers.flujo_eliminar_booking import flujoEliminarBooking
from controllers.flujo_actualizar_booking import FlujoActualizarBooking
from controllers.flujo_obtener_booking_id import FlujoObtenerBookingId
from controllers.flujo_comprobar_conexion import flujoComprobarConexion
from controllers.flujo_modificarPar_booking import FlujoModificarParBooking


class Application:
    def __init__(self):
        self.flujoObtenerToken = FlujoObtenerToken()
        self.flujoCrearBooking = FlujoCrearBooking()
        self.flujoObtenerBooking = FlujoObtenerBooking()
        self.flujoObtenerBookingId = FlujoObtenerBookingId()
        self.flujoEliminarBooking = flujoEliminarBooking()
        self.flujoActualizarBooking = FlujoActualizarBooking()
        self.flujoComprobarConexion = flujoComprobarConexion()
        self.flujoModificarParBooking = FlujoModificarParBooking()
