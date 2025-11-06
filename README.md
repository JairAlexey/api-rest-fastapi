# Taller 02 – API REST de Envíos (FastAPI)

Proyecto de referencia para el Taller 02 – Diseño e Implementación de una API REST.
La API gestiona “envíos” para una empresa logística, aplicando diseño RESTful,
documentación OpenAPI y ejecución reproducible con Docker.

## Estructura del proyecto

```
api-rest-fastapi/
├─ app/
│  ├─ main.py
│  ├─ models.py
│  ├─ storage.py
│  └─ __init__.py
├─ requirements.txt
├─ export_openapi.py
├─ Dockerfile
├─ README.md
├─ postman_collection.json
└─ openapi.json
```

## Requisitos

- Python 3.11+
- Docker (opcional para ejecución en contenedor)
- Postman (para importar la colección)

## Instalación y ejecución

### Opción A: Entorno virtual (recomendado en desarrollo)

```bash
python -m venv .venv
# Linux/MacOS
. .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

La API quedará disponible en:
- Swagger UI: http://localhost:8080/docs
- OpenAPI JSON: http://localhost:8080/openapi.json

### Opción B: Docker (reproducible)

```bash
docker build -t api-rest-fastapi .
docker run -p 8080:8080 api-rest-fastapi
```

La API quedará disponible en:
- Swagger UI: http://localhost:8080/docs
- OpenAPI JSON: http://localhost:8080/openapi.json

## Exportar contrato OpenAPI

Este proyecto incluye un script para exportar el contrato OpenAPI sin levantar el servidor.

```bash
python export_openapi.py
```

Esto generará/actualizará el archivo `openapi.json` en la raíz del proyecto.

## Pruebas con Postman

- Importa el archivo `postman_collection.json` en Postman.
- La colección incluye:
  - GET `/health`
  - GET `/envios`
  - GET `/envios/001`
  - POST `/envios` (con cuerpo de ejemplo)
- Variable `baseUrl` por defecto: `http://localhost:8080`.

## Endpoints y ejemplos

- GET `/health`
  - Respuesta: `{ "status": "ok" }`

- GET `/envios`
  - Lista todos los envíos.

- GET `/envios/{id}`
  - 404 si no existe.

- POST `/envios`
  - Crea un nuevo envío. 409 si el `id` ya existe.
  - Ejemplo de cuerpo:

```json
{
  "id": "002",
  "destinatario": "María Gómez",
  "direccion": "Calle 10 #5-20",
  "estado": "Preparando"
}
```

## Evidencias sugeridas

Incluye en la entrega capturas de pantalla de:
- Swagger UI en `/docs` mostrando los endpoints.
- Ejecución exitosa de cada endpoint desde Postman.
- Logs del contenedor al ejecutar con Docker (por ejemplo: línea de arranque de `uvicorn`).

## Notas de implementación

- Almacenamiento en memoria en `app/storage.py` con un registro precargado:
  - `001`: Juan Pérez, Av. Siempre Viva 742, En tránsito.
- Modelo `Envio` definido con Pydantic en `app/models.py`.
- Servidor con `uvicorn` expuesto en el puerto 8080.
