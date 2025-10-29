from __future__ import annotations

from threading import RLock
from typing import Dict, List, Optional

from .models import Envio


class InMemoryEnvioStorage:
    def __init__(self) -> None:
        self._lock = RLock()
        self._envios_by_id: Dict[str, Envio] = {
            "001": Envio(
                id="001",
                destinatario="Juan Pérez",
                direccion="Av. Siempre Viva 742",
                estado="En tránsito",
            )
        }

    def list_envios(self) -> List[Envio]:
        with self._lock:
            return list(self._envios_by_id.values())

    def get_envio(self, envio_id: str) -> Optional[Envio]:
        with self._lock:
            return self._envios_by_id.get(envio_id)

    def create_envio(self, envio: Envio) -> bool:
        with self._lock:
            if envio.id in self._envios_by_id:
                return False
            self._envios_by_id[envio.id] = envio
            return True


storage = InMemoryEnvioStorage()
