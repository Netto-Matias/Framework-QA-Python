from pages.the_internet.PaginaDropdown import PaginaDropdown

def test_seleccionar_opcion_dropdown(driver):
    pagina_dropdown = PaginaDropdown(driver)
    
    # 1. Navego a la página del dropdown
    pagina_dropdown.navegar()
    
    # 2. Selecciono una opción del dropdown
    opcion_a_seleccionar = "Option 1"
    pagina_dropdown.seleccionar_opcion_por_texto(opcion_a_seleccionar)
    
    # 3. Verifico que quedó seleccionada
    opcion_seleccionada = pagina_dropdown.obtener_opcion_seleccionada()
    
    assert opcion_seleccionada == opcion_a_seleccionar
    
    # 4. Selecciono otra opción del dropdown
    pagina_dropdown.seleccionar_opcion_por_texto("Option 2")	
    assert pagina_dropdown.obtener_opcion_seleccionada() == "Option 2"