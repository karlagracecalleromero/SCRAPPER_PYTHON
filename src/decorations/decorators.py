import time  # Importación del módulo time para medir el tiempo de ejecución
import logging  # Importación del módulo logging para registrar mensajes

# Configurar el logger para mostrar mensajes de nivel INFO en la consola
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Decorador para medir el tiempo de ejecución de una función
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Registrar el tiempo de inicio
        result = func(*args, **kwargs)  # Ejecutar la función
        final_time = time.time()  # Registrar el tiempo de finalización
        elapsed_time = final_time - start_time  # Calcular el tiempo transcurrido
        # Registrar el tiempo de ejecución en el logger
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:.4f} segundos")
        return result
    return wrapper

# Decorador para registrar mensajes antes y después de la ejecución de una función
def logit(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")  # Mensaje de inicio de ejecución
        result = func(*args, **kwargs)  # Ejecutar la función
        logging.info(f"Completado {func.__name__}")  # Mensaje de finalización de ejecución
        return result
    return wrapper

