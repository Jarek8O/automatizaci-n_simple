from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar

# Configuración Selenium
options = Options()
# comenta esto si quieres ver el navegador
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Detecta qué quiere el usuario
def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    elif "salir" in user_input:
        return "salir"
    return None

print("Hola, soy tu chatbot. Escribe 'salir' para terminar.")

while True:
    user_input = sanitizar(input("---> "))
    funcion = procesar_input(user_input)

    if funcion == "salir":
        print("Adiós 👋")
        break

    if funcion is None:
        print("No entendí, intenta otra vez.")
    else:
        respuesta = funcion(driver, user_input)
        print(f">>> {respuesta}")

