"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : theme_manager.py
Módulo      : Core
Descripción : Gestiona la configuración visual global de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication


class ThemeManager:
    """
    Administra el tema visual de FarmaciaPOS.
    """

    # Colores principales
    PRIMARY_COLOR = "#2563EB"
    PRIMARY_DARK = "#1D4ED8"
    SUCCESS_COLOR = "#16A34A"
    WARNING_COLOR = "#D97706"
    ERROR_COLOR = "#DC2626"

    # Escala de grises
    BACKGROUND_COLOR = "#F5F7FA"
    SURFACE_COLOR = "#FFFFFF"
    BORDER_COLOR = "#D9DEE7"

    TEXT_PRIMARY = "#1F2937"
    TEXT_SECONDARY = "#6B7280"

    # Tipografía
    FONT_FAMILY = "Segoe UI"
    FONT_SIZE_SMALL = 12
    FONT_SIZE_NORMAL = 13
    FONT_SIZE_LARGE = 16
    FONT_SIZE_TITLE = 24

    # Espaciados
    SPACING_XS = 4
    SPACING_SM = 8
    SPACING_MD = 16
    SPACING_LG = 24
    SPACING_XL = 32

    # Bordes
    BORDER_RADIUS = 8

    @classmethod
    def apply(cls, application: QApplication) -> None:
        """
        Aplica el tema visual global.
        """
        application.setStyleSheet(cls.stylesheet())

    @classmethod
    def stylesheet(cls) -> str:
        """
        Retorna la hoja de estilos global.
        """
        return f"""
        * {{
            font-family: "{cls.FONT_FAMILY}";
            font-size: {cls.FONT_SIZE_NORMAL}px;
            color: {cls.TEXT_PRIMARY};
        }}

        QMainWindow {{
            background-color: {cls.BACKGROUND_COLOR};
        }}

        QWidget {{
            background-color: {cls.BACKGROUND_COLOR};
        }}

        QLabel {{
            background: transparent;
            color: {cls.TEXT_PRIMARY};
        }}

        QPushButton {{
            background-color: {cls.PRIMARY_COLOR};
            color: white;
            border: none;
            border-radius: {cls.BORDER_RADIUS}px;
            padding: 8px 16px;
            font-weight: 600;
        }}

        QPushButton:hover {{
            background-color: {cls.PRIMARY_DARK};
        }}

        QPushButton:pressed {{
            background-color: {cls.PRIMARY_DARK};
        }}

        QLineEdit,
        QTextEdit,
        QPlainTextEdit,
        QComboBox {{
            background: {cls.SURFACE_COLOR};
            border: 1px solid {cls.BORDER_COLOR};
            border-radius: {cls.BORDER_RADIUS}px;
            padding: 6px;
        }}
        """

    @classmethod
    def primary_color(cls) -> QColor:
        """
        Retorna el color principal como QColor.
        """
        return QColor(cls.PRIMARY_COLOR)