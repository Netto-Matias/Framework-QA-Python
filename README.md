# Framework de Automatización de QA (Selenium + Pytest + API)

Este es mi proyecto de portafolio de automatización de QA, construido desde cero. 

## Proposito

Demostrar habilidades en la creación de un framework de pruebas escalable y mantenible usando Python

## Tecnologías utilizadas

* **Python 3**
* **Selenium:** Para la automatización de UI (Frontend).
* **Pytest:** Como test runner y para la gestión de fixtures (Setup/Teardown).
* **Requests:** Para la automatización de API (Backend).
* **Page Object Model (POM):** Como patrón de diseño para la mantenibilidad.

## Pruebas incluidas
 
* **API (JSONPlaceholder):** Pruebas de `GET` y `POST`. 
* **UI (SauceDemo):**
    * Flujos de Login (Happy/Sad Path).
    * **[NUEVO]** Flujo E2E de Compra Completa: Login -> Selección de Productos -> Carrito -> Checkout -> Validación de Orden.
    * Uso de Page Object Model en cada pantalla (Login, Inventario, Carrito, Checkout).
      
## Cómo ejecutarlo

1. Clonar el repositorio: `git clone ...`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar todas las pruebas: `pytest`
