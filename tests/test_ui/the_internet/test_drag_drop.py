from pages.the_internet.PaginaDragDrop import PaginaDragDrop

def test_intercambio_cajas(driver):
    page = PaginaDragDrop(driver)
    page.navegar()
    
    # Verificar estado incial 
    assert page.obtener_texto_caja_a() == "A"
    assert page.obtener_texto_caja_b() == "B"
    
    page.arrastrar_a_hacia_b()
    
    # Verificar estado final
    
    assert page.obtener_texto_caja_a() == "B"
    assert page.obtener_texto_caja_b() == "A"