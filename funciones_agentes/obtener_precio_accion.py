from selenium.webdriver.common.by import By

def obtener_precio_accion(driver, consulta):
    driver.get(f"https://www.google.com/search?q=precio+accion+{consulta}")

    try:
        empresa = driver.find_element(By.CSS_SELECTOR, "div[class='PZPZlf ssJ7i B5dxMb']").text
        precio = driver.find_element(By.CSS_SELECTOR, "span[jsname='vWLAgc']").text
        
        # divisa (ej: USD)
        divisa = driver.find_element(By.CSS_SELECTOR, "span[jsname='vWLAgc']").get_attribute("aria-label").split()[-1]
        
        # ticker (ej: NASDAQ: MSFT)
        ticker = driver.find_element(By.CSS_SELECTOR, "div[class='zzDege']").text

        return f"{empresa} [{ticker}] ${precio} {divisa}."
    except:
        return "No se pudo obtener el precio de la acción."
