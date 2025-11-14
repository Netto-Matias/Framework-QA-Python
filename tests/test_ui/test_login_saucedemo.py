from selenium import webdriver
from pages.PaginaLogin import PaginaLogin

def test_login_valido():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_page = PaginaLogin(driver)
    login_page.iniciar_sesion("standard_user", "secret_sauce")
    
    # "Afirmo que la URL actual ES IGUAL a la esperada"

    url_esperada = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == url_esperada
    
    driver.quit()

def test_login_invalido():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_page = PaginaLogin(driver)
    login_page.iniciar_sesion("standard_user", "password_mala")
    
    texto_esperado = "Epic sadface: Username and password do not match any user in this service"
    texto_actual = login_page.obtener_mensaje_error()
    
    assert texto_actual == texto_esperado
    
    driver.quit()
    