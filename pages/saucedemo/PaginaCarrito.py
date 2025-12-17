from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginaCarrito:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.locator_nombres_productos = (By.CLASS_NAME, "inventory_item_name")
        self.locator_boton_checkout = (By.ID, "checkout")
        
    def obtener_nombres_carrito(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.locator_nombres_productos))
        productos = self.driver.find_elements(*self.locator_nombres_productos)
        
        # Lista limpia solo con los nombres
        nombres = [producto.text for producto in productos]
        return nombres
    
    def hacer_checkout(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.locator_boton_checkout))
        
        # Uso de JavaScript para hacer clic forzado
        self.driver.execute_script("arguments[0].click();", boton)