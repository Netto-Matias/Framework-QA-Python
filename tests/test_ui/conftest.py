import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    print("\n[SETUP] Creando instancia del driver...")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    d = webdriver.Chrome()
    
    yield d
    
    print("\n[TEARDOWN] Cerrando instancia del driver...")
    d.quit()