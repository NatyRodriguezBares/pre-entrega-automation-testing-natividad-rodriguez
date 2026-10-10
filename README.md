# Pre-entrega - Automation Testing

## ¿De qué va el proyecto?

Este proyecto consiste en hacer pruebas automatizadas en la web SauceDemo para comprobar que las funciones principales funcionan correctamente.

## Herramientas utilizadas

- Python
- Selenium
- Pytest
- WebDriver Manager
- Pytest HTML

## Carpetas y archivos

- `tests/`: contiene las pruebas que he ido haciendo.
- `pages/`: contiene la página de inicio de sesión.
- `utils/`: contiene la configuración de los registros de ejecución.
- `reports/`: aquí se guardan el informe HTML, los registros y las capturas cuando una prueba falla.
- `requirements.txt`: lista de las dependencias necesarias.
- `datos/`: se puede utilizar si más adelante necesito datos externos.

## Cómo instalarlo

Primero hay que descargar el proyecto y abrirlo desde la terminal. Después, crear y activar un entorno virtual e instalar las dependencias.

En Windows, para crear el entorno virtual:

`python -m venv .venv`

Para activarlo desde Git Bash:

`source .venv/Scripts/activate`

Después, instalar las dependencias con este comando:

`python -m pip install -r requirements.txt`

## Cómo ejecutar las pruebas

Desde la carpeta principal del proyecto, ejecutar:

`python -m pytest tests/ -v --html=reports/reporte.html --self-contained-html`

## Informes y evidencias

El proyecto genera un informe HTML con los resultados de las pruebas. También guarda un registro de ejecución y hace capturas de pantalla cuando alguna prueba falla.

- Informe: `reports/reporte.html`
- Registro: `reports/ejecucion.log`
- Capturas: `reports/capturas/`

Actualmente hay 10 pruebas automatizadas que comprueban el inicio de sesión, los productos, el carrito, el orden de los precios y el cierre de sesión.