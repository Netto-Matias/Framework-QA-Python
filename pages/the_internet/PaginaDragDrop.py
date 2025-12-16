from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains 

class PaginaDragDrop: 
    
    def __init__(self, driver): 
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.box_a = (By.ID, "column-a")
        self.box_b = (By.ID, "column-b")
        
        # Locators del encabezado dentro de las cajas
        self.header_box_a = (By.CSS_SELECTOR, "#column-a header")
        self.header_box_b = (By.CSS_SELECTOR, "#column-b header")
        
    def navegar(self):
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        
    def arrastrar_a_hacia_b(self): 
        origen = self.wait.until(EC.visibility_of_element_located(self.box_a))
        destino = self.wait.until(EC.visibility_of_element_located(self.box_b))
        
        actions = ActionChains(self.driver)
        
        actions.drag_and_drop(origen, destino)
        
        actions.perform()
        
    def obtener_texto_caja_a(self):
        return self.driver.find_element(*self.header_box_a).text
    
    def obtener_texto_caja_b(self):
        return self.driver.find_element(*self.header_box_b).text
    
    