from pages.saucedemo.PaginaLogin import PaginaLogin

def test_login_valido(driver):
    login_page = PaginaLogin(driver)
    login_page.iniciar_sesion("standard_user", "secret_sauce")
    
    url_esperada = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == url_esperada
    
def test_login_invalido(driver):
    login_page = PaginaLogin(driver)
    login_page.iniciar_sesion("standard_user", "wrong_password")
    
    text_esperado = "Epic sadface: Username and password do not match any user in this service"
    text_obtenido = login_page.obtener_mensaje_error()
    
    assert text_obtenido == text_esperado