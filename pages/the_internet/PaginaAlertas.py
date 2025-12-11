from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginaAlertas:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators de los botones que disparan las alertas
        self.btn_alert = (By.XPATH, "//button[text()='Click for JS Alert']")
        self.btn_confirm = (By.XPATH, "//button[text()='Click for JS Confirm']")
        self.btn_prompt = (By.XPATH, "//button[text()='Click for JS Prompt']")
        
        # Locator del teto de resultado
        self.txt_result = (By.ID, "result")
        
    def navegar(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        
    # --- Acciones para disparar las alertas ---
    def click_boton_alerta(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_alert)).click()
        
    def click_boton_confirm(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_confirm)).click()
    
    def click_boton_prompt(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_prompt)).click()
        
    # --- Manejo de las alertas ---
    
    def aceptar_alerta(self):
        self.wait.until(EC.alert_is_present())
        alerta = self.driver.switch_to.alert
        alerta.accept()
        
    def cancelar_alerta(self):
        self.wait.until(EC.alert_is_present())
        alerta = self.driver.switch_to.alert
        alerta.dismiss()
    
    def escribir_en_alerta(self, texto): 
        self.wait.until(EC.alert_is_present())
        alerta = self.driver.switch_to.alert
        alerta.send_keys(texto)
        alerta.accept()
        
    def obtener_resultado(self):
        return self.wait.until(EC.visibility_of_element_located(self.txt_result)).text
