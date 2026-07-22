"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : main.py
Módulo      : Core
Descripción : Punto de entrada de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from src.core.application import Application


def main() -> None:
    """
    Punto de entrada de FarmaciaPOS.
    """
    application = Application()
    application.run()


if __name__ == "__main__":
    main()