from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_clima(driver, consulta):
    driver.get(f"https://www.google.com/search?q=clima+{consulta}")

    try:
        # Espera hasta que aparezca la temperatura (esto incluye tiempo para captcha)
        wait = WebDriverWait(driver, 30)

        temperatura = wait.until(
            EC.presence_of_element_located((By.ID, "wob_tm"))
        ).text

        ubicacion = driver.find_element(By.ID, "wob_loc").text
        estado = driver.find_element(By.ID, "wob_dc").text

        return f"{ubicacion}: {temperatura}°C, {estado}."

    except:
        return "No se pudo obtener el clima."
