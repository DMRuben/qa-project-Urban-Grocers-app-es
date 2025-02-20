# Proyecto Urban Grocers 
# Proyecto de API para Crear un Kit de Usuario

Este proyecto tiene como objetivo probar la creación de un kit para un usuario a través de una API.

## Requisites

- Python version de las mas nuevas
- Pytest
- Bajar las librerias "REQUESTS" y "PYTEST"

## Instrucciones

1. Clona el repositorio de acuerdo a las instrucciones de 310
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta las pruebas: `pytest`.

Las pruebas están diseñadas para verificar las restricciones de caracteres en el campo "name" al crear un kit para un usuario.

## Archivos del Proyecto

- `configuration.py`: Configuración de la URL y rutas de la API de acuerdo a la documentacion.
- `data.py`: Contiene los cuerpos de las solicitudes POST para las pruebas.
- `sender_stand_request.py`: Funciones para enviar las solicitudes.
- `create_kit_name_kit_test.py`: Archivos de pruebas unitarias usando Pytest.
