import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\n[SETUP] Creando instancia del driver...")
    d = webdriver.Chrome()
    d.get("https://www.saucedemo.com/")
    
    yield d
    
    print("\n[TEARDOWN] Cerrando instancia del driver...")
    d.quit()