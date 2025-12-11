from selenium.webdriver.common.by import By

class PaginaLogin:
    
    def __init__(self, driver):
        self.driver = driver
        
        self.locator_usuario = (By.ID, "user-name")
        self.locator_password = (By.ID, "password")
        self.locator_boton_login = (By.ID, "login-button")
        self.locator_error_message = (By.XPATH, "//*[@data-test='error']")
    
    def navegar(self):
        self.driver.get("https://www.saucedemo.com/")
        
    def escribir_usuario(self, usuario):
        self.driver.find_element(*self.locator_usuario).send_keys(usuario)
    
    def escribir_password(self, password):
        self.driver.find_element(*self.locator_password).send_keys(password)
        
    def clic_login(self):
        self.driver.find_element(*self.locator_boton_login).click()
    
    def iniciar_sesion(self, usuario, password):
        self.escribir_usuario(usuario)
        self.escribir_password(password)
        self.clic_login()
    
    def obtener_mensaje_error(self):
        return self.driver.find_element(*self.locator_error_message).text