from pydantic import BaseModel, Field


class Envio(BaseModel):
    id: str = Field(..., description="Identificador único del envío")
    destinatario: str = Field(..., description="Nombre del destinatario")
    direccion: str = Field(..., description="Dirección de entrega")
    estado: str = Field(..., description="Estado actual del envío")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "001",
                "destinatario": "Juan Pérez",
                "direccion": "Av. Siempre Viva 742",
                "estado": "En tránsito",
            }
        }
