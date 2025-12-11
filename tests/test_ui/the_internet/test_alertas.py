from pages.the_internet.PaginaAlertas import PaginaAlertas

def test_manejo_alertas(driver):
    page = PaginaAlertas(driver)
    page.navegar()
    
    # CASO 1: Aceptar una alerta simple
    page.click_boton_alerta()
    page.aceptar_alerta()
    assert page.obtener_resultado() == "You successfully clicked an alert"
    
    # CASO 2: Cancelar una alerta de confirmación
    page.click_boton_confirm()
    page.cancelar_alerta()
    assert page.obtener_resultado() == "You clicked: Cancel"
    
    # CASO 3: Prompt
    texto_prompt = "Texto de prueba"
    page.click_boton_prompt()
    page.escribir_en_alerta(texto_prompt)
    assert f"You entered: {texto_prompt}" in page.obtener_resultado()