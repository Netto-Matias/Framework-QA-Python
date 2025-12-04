from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginaCheckout:
    
    def __init__(self, driver): 
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   
        
        # Locators del formulario
        self.locator_input_nombre = (By.ID, "first-name")
        self.locator_input_apellido = (By.ID, "last-name")
        self.locator_input_codigo_postal = (By.ID, "postal-code")
        self.locator_botton_continue = (By.ID, "continue")
        
        # Locators de finalización
        self.locator_boton_terminar = (By.ID, "finish")
        self.locator_mensaje_exito = (By.CLASS_NAME, "complete-header")
        
    def llenar_formulario(self, nombre, apellido, codigo_postal):
        self.wait.until(EC.visibility_of_element_located(self.locator_input_nombre)).send_keys(nombre)
        self.driver.find_element(*self.locator_input_apellido).send_keys(apellido)
        self.driver.find_element(*self.locator_input_codigo_postal).send_keys(codigo_postal)
        self.driver.find_element(*self.locator_botton_continue).click()
        
    def finalizar_compra(self):
        self.wait.until(EC.element_to_be_clickable(self.locator_boton_terminar)).click()
    
    def obtener_mensaje_exito(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_mensaje_exito)).text