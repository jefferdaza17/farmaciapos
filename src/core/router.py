"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : router.py
Módulo      : Core
Descripción : Gestiona la navegación entre los módulos de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from typing import Dict

from PySide6.QtWidgets import QWidget

from src.ui.shell.workspace import Workspace


class Router:
    """
    Gestiona la navegación entre páginas.
    """

    def __init__(self, workspace: Workspace) -> None:
        """
        Inicializa el Router.
        """
        self._workspace = workspace
        self._pages: Dict[str, QWidget] = {}

    def register(self, name: str, page: QWidget) -> None:
        """
        Registra una página.
        """
        if name in self._pages:
            raise ValueError(
                f'La página "{name}" ya fue registrada.'
            )

        self._pages[name] = page
        self._workspace.add_page(page)

    def navigate(self, name: str) -> None:
        """
        Navega hacia una página.
        """
        page = self._pages.get(name)

        if page is None:
            raise KeyError(
                f'La página "{name}" no existe.'
            )

        self._workspace.set_current_page(page)

    def exists(self, name: str) -> bool:
        """
        Indica si una página existe.
        """
        return name in self._pages

    def page(self, name: str) -> QWidget:
        """
        Retorna una página registrada.
        """
        if name not in self._pages:
            raise KeyError(
                f'La página "{name}" no existe.'
            )

        return self._pages[name]

    def pages(self) -> dict[str, QWidget]:
        """
        Retorna todas las páginas registradas.
        """
        return self._pages.copy()