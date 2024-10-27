import mysql.connector
import logging
import json
import os

from mysql.connector import errorcode

logger = logging.getLogger("mysql.connector")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


def obtener_config_db():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = base_path + "/config.json"
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        logger.error("El archivo de configuración no se encontró.")
    except json.JSONDecodeError:
        logger.error("Error al decodificar el archivo de configuración.")
    return None


def conexion_bd():
    config = obtener_config_db()
    if config is None:
        return None

    try:
        conn = mysql.connector.connect(
            user=config.get("user"),
            password=config.get("password"),
            host=config.get("host"),
            database=config.get("database"),
            port=config.get("port", 3306),
        )
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(
                "------------------------------------------------------------------------------------------"
            )
            logger.error("  Usuario o Password no válido       |")
            print(
                "Por favor configure correctamente sus credenciales en el archivo core/DAO/config.json    |"
            )
            print(
                "------------------------------------------------------------------------------------------"
            )
            exit(1)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("La base de datos no existe.")
        else:
            logger.error(f"Error desconocido: {err}")
    return None
