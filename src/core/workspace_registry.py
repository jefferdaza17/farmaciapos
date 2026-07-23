"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : workspace_registry.py
Módulo      : Core
Descripción : Registro central de los módulos de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from dataclasses import dataclass
from typing import Dict

from PySide6.QtWidgets import QWidget


@dataclass(frozen=True)
class WorkspaceItem:
    """
    Representa un módulo registrado.
    """

    id: str
    title: str
    icon: str
    order: int
    page: QWidget


class WorkspaceRegistry:
    """
    Administra el registro de módulos.
    """

    def __init__(self) -> None:
        """
        Inicializa el registro.
        """
        self._items: Dict[str, WorkspaceItem] = {}

    def register(self, item: WorkspaceItem) -> None:
        """
        Registra un nuevo módulo.
        """
        if item.id in self._items:
            raise ValueError(
                f'El módulo "{item.id}" ya se encuentra registrado.'
            )

        self._items[item.id] = item

    def unregister(self, module_id: str) -> None:
        """
        Elimina un módulo del registro.
        """
        self._items.pop(module_id, None)

    def exists(self, module_id: str) -> bool:
        """
        Indica si un módulo existe.
        """
        return module_id in self._items

    def get(self, module_id: str) -> WorkspaceItem:
        """
        Retorna un módulo.
        """
        if module_id not in self._items:
            raise KeyError(
                f'El módulo "{module_id}" no existe.'
            )

        return self._items[module_id]

    def all(self) -> list[WorkspaceItem]:
        """
        Retorna todos los módulos ordenados.
        """
        return sorted(
            self._items.values(),
            key=lambda item: item.order
        )

    def clear(self) -> None:
        """
        Elimina todos los módulos.
        """
        self._items.clear()

    def count(self) -> int:
        """
        Retorna la cantidad de módulos registrados.
        """
        return len(self._items)