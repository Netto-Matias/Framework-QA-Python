# 🚀 Framework de Automatización de QA (Híbrido: UI + API)

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-API_Testing-orange?style=for-the-badge)

Este repositorio aloja un framework de pruebas automatizadas robusto y escalable, diseñado para validar tanto interfaces de usuario (Frontend) como servicios web (Backend/API).

El proyecto simula un entorno de QA real, integrando patrones de diseño avanzados, reportes visuales y manejo de escenarios complejos.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3
* **Web Automation:** Selenium WebDriver
* **API Automation:** Requests Library
* **Test Runner:** Pytest
* **Reportes:** Pytest-HTML
* **Patrón de Diseño:** Page Object Model (POM)

---

## 🧠 Conceptos Clave Implementados

Este es un framework completo que demuestra:

* **Page Object Model (POM):** Separación estricta entre la lógica de prueba y la estructura de la página para máxima mantenibilidad.
* **Arquitectura Escalable:** Estructura modular separada por dominios (`pages/saucedemo`, `pages/the_internet`).
* **Manejo de Esperas:** Uso exclusivo de **Explicit Waits** (`WebDriverWait`) para sincronización robusta (cero `time.sleep`).
* **Elementos Complejos:** Manejo de Shadow DOM, iFrames, **Alertas de JavaScript**, Dropdowns nativos (`Select`) y acciones de mouse (**Drag & Drop**).
* **Fixtures de Pytest:** Gestión eficiente del ciclo de vida del `driver` (Setup/Teardown).

---

## 🧪 Escenarios de Prueba Cubiertos

### 1. E-Commerce (SauceDemo)
Automatización de flujos críticos de negocio.
* ✅ **Login:** Validación de Happy Path y Sad Path (usuarios bloqueados/incorrectos).
* ✅ **Flujo E2E de Compra:** Login -> Catálogo -> Carrito -> Checkout -> Finalización.
* ✅ **Validación de Datos:** Verificación de ítems en el carrito y cálculo de totales.

### 2. "QA Gym" (The Internet Herokuapp)
Pruebas técnicas sobre elementos web difíciles.
* ✅ **Alertas JS:** Manejo de `Alert`, `Confirm` y `Prompt` (con `Switch To`).
* ✅ **Dropdowns:** Selección de opciones en elementos `<select>` nativos.
* ✅ **Drag and Drop:** Simulación de arrastrar y soltar elementos usando `ActionChains`.

### 3. API REST (JSONPlaceholder)
Validación de Backend.
* ✅ **Métodos HTTP:** Pruebas de `GET` (listados) y `POST` (creación de recursos).
* ✅ **Validaciones:** Códigos de estado (200, 201) y estructura del JSON de respuesta.

---

## ⚙️ Instalación y Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Netto-Matias/Framework-QA-Python.git](https://github.com/Netto-Matias/Framework-QA-Python.git)
    cd Framework-QA-Python
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar pruebas (Básico):**
    ```bash
    pytest
    ```

4.  **Ejecutar pruebas con Reporte HTML:**
    ```bash
    pytest --html=reporte_pruebas.html
    ```

---

## 📊 Reporte de Ejecución

El framework genera automáticamente un reporte detallado en HTML con el estado de cada prueba.

<img width="1872" height="662" alt="Captura de pantalla 2025-12-15 231336" src="https://github.com/user-attachments/assets/e87597a8-137e-49a9-84c8-8197185bb7ed" />

---

**Autor:** Matías Netto - [LinkedIn](https://www.linkedin.com/in/matias-netto)


