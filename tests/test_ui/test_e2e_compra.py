from pages.PaginaLogin import PaginaLogin
from pages.PaginaCarrito import PaginaCarrito
from pages.PaginaInventario import PaginaInventario
from pages.PaginaChechout import PaginaCheckout

def test_flujo_compra_completo(driver):
    # 1. LOGIN
    login_page = PaginaLogin(driver)
    login_page.iniciar_sesion("standard_user", "secret_sauce")
    
    # 2. Inventario
    inventario_page = PaginaInventario(driver)
    
    producto_1 = "Sauce Labs Backpack"
    producto_2 = "Sauce Labs Fleece Jacket"
    
    inventario_page.agregar_carrito(producto_1)
    inventario_page.agregar_carrito(producto_2)
    
    # Ir al carrito 
    inventario_page.ir_al_carrito()
    
    # 3. Carrito
    carrito_page = PaginaCarrito(driver)
    carrito_page.hacer_checkout()
    
    # 4. Checkout
    checkout_page = PaginaCheckout(driver)
    checkout_page.llenar_formulario("Matías", "QA1234", "1234")
    
    # Finalización
    checkout_page.finalizar_compra()
    
    # Verificación
    mensaje = checkout_page.obtener_mensaje_exito()
    assert mensaje == "Thank you for your order!"
    
    print("PASS: Flujo de compra completo exitoso.")
    
    
    