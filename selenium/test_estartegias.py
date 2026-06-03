from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = None

try:
    # ✅ Configuración
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # ✅ Abrir página
    driver.get("https://www.estraitegias.com")

    wait = WebDriverWait(driver, 15)

    # ✅ Esperar a que desaparezca el preloader
    wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
    print("✅ Preloader desapareció")

    # ✅ Click en Contacto (con JS para evitar errores)
    contacto = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contacto")))
    driver.execute_script("arguments[0].click();", contacto)
    print("✅ Click en Contacto")

    # ✅ Esperar sección contacto
    seccion = wait.until(EC.presence_of_element_located((By.ID, "tab-contact")))

    # ✅ Scroll a la sección
    driver.execute_script("arguments[0].scrollIntoView(true);", seccion)
    print("✅ Scroll hacia sección contacto")

    time.sleep(2)

    # ✅ Validar que la sección está visible
    assert seccion.is_displayed()
    print("✅ Sección visible")

    # ✅ Buscar emails usando mailto (forma correcta)
    emails = driver.find_elements(By.XPATH, "//a[contains(@href,'mailto')]")

    email_encontrado = False

    for email in emails:
        if email.is_displayed() and email.text != "":
            print("✅ Email visible:", email.text)
            email_encontrado = True
            break

    if not email_encontrado:
        raise Exception("No se encontró ningún email visible")

except Exception as e:
    print("❌ Error encontrado:", e)

    if driver:
        driver.save_screenshot("error.png")
        print("📸 Screenshot guardado como error.png")

finally:
    time.sleep(5)
    if driver:
        driver.quit()
