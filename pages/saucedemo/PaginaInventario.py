from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginaInventario:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.locator_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.locator_badge_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        
    def agregar_carrito(self, nombre_exacto):
        nombre_formateado = nombre_exacto.lower().replace(" ", "-")
        locator_boton = (By.ID, f"add-to-cart-{nombre_formateado}") 
        
        boton = self.wait.until(EC.element_to_be_clickable(locator_boton))
        boton.click()
        
    def obtener_numero_carrito(self):
        try:
            badge = self.wait.until(EC.visibility_of_element_located(self.locator_badge_carrito))
            return int(badge.text)
        except:
            return 0
        
    def ir_al_carrito(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.locator_boton_carrito))
        
        self.driver.execute_script("arguments[0].click();", boton)
        