from django.db import connections, OperationalError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class DatabaseConnectionFactory:
    _connection_name = 'default'  # Puedes cambiar el nombre según tu configuración

    @classmethod
    def get_connection(cls):
        """
        Obtiene una conexión de la base de datos.
        Si la conexión no está activa, intenta reconectar.
        """
        try:
            connection = connections[cls._connection_name]
            # Verificar si la conexión está activa
            if not connection.is_usable():
                logger.warning(f"Conexión '{cls._connection_name}' no usable. Reconectando...")
                connection.close()
                connection.connect()
            return connection
        except OperationalError as e:
            logger.error(f"Error al conectar con la base de datos '{cls._connection_name}': {e}")
            raise Exception(f"Error al conectar con la base de datos: {e}")
        except Exception as e:
            logger.error(f"Excepción no controlada en la conexión: {e}")
            raise Exception(f"Excepción no controlada: {e}")

    @classmethod
    def close_connection(cls):
        """
        Cierra una conexión específica.
        """
        try:
            connection = connections[cls._connection_name]
            if connection and not connection.closed_in_transaction:
                connection.close()
                logger.info(f"Conexión '{cls._connection_name}' cerrada correctamente.")
        except Exception as e:
            logger.error(f"Error al cerrar la conexión '{cls._connection_name}': {e}")
            raise Exception(f"Error al cerrar la conexión: {e}")

    @classmethod
    def close_all_connections(cls):
        """
        Cierra todas las conexiones activas.
        """
        try:
            connections.close_all()
            logger.info("Todas las conexiones han sido cerradas correctamente.")
        except Exception as e:
            logger.error(f"Error al cerrar todas las conexiones: {e}")
            raise Exception(f"Error al cerrar todas las conexiones: {e}")
