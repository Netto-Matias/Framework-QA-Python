from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class PaginaDropdown:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.dropdown_locator = (By.ID, "dropdown")
        
    def navegar(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
        
    def seleccionar_opcion_por_texto(self, texto_opcion):
        # 1. Espero a que el elemento sea visible
        elemento_select = self.wait.until(EC.visibility_of_element_located(self.dropdown_locator))
        
        # 2. "Envuelvo" el elemento en un objeto Select
        dropdown = Select(elemento_select)
        
        # 3. Selecciono la opción por su texto visible
        dropdown.select_by_visible_text(texto_opcion)
        
    def obtener_opcion_seleccionada(self):
        elemento_select = self.wait.until(EC.visibility_of_element_located(self.dropdown_locator))
        dropdown = Select(elemento_select)
        
        return dropdown.first_selected_option.text # Devuelvo el elemento que está activo
    
    