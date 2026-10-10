
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_verificar_inventario(driver):
    assert driver.title == "Swag Labs", "El título de la página no es correcto"
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products", "No se muestra el título Products"



def test_productos_visibles(driver):
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(productos) > 0, "No se encontraron productos visibles"

    primer_producto = productos[0]
    nombre = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    precio = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    print(f"Primer producto: {nombre} - Precio: {precio}")




def test_validar_interfaz(driver):
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), "El menú no está visible"
    assert filtro.is_displayed(), "El filtro de productos no está visible"


def test_anadir_producto_al_carrito(driver):
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".inventory_item button"), "Remove"
        )
    )

    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
    assert boton_agregar.text == "Remove", "El botón no cambió a Remove"


def test_verificar_contador_carrito(driver):
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    assert contador == "1", f"Se esperaba 1 producto, pero apareció {contador}"



def test_navegar_al_carrito(driver):
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    primer_producto.find_element(By.TAG_NAME, "button").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "/cart.html" in driver.current_url, "No se abrió la página del carrito"


def test_comprobar_producto_en_carrito(driver):
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre_esperado = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    primer_producto.find_element(By.TAG_NAME, "button").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    nombre_carrito = driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    assert nombre_carrito == nombre_esperado, "El producto del carrito no coincide"


def test_ordenar_productos(driver):
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    filtro.click()

    filtro.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()

    precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    valores = [float(precio.text.replace("$", "")) for precio in precios]

    assert valores == sorted(valores), "Los productos no se ordenaron por precio de menor a mayor"



def test_cerrar_sesion(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()

    logout = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )

    driver.execute_script("arguments[0].click();", logout)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    assert driver.current_url == "https://www.saucedemo.com/"





