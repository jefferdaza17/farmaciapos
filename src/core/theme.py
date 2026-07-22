from pathlib import Path

from PySide6.QtWidgets import QApplication

from src.core.config import ROOT_DIR


class ThemeManager:
    @staticmethod
    def load(app: QApplication) -> None:
        theme_file = Path(ROOT_DIR) / "assets" / "styles" / "theme.qss"

        if not theme_file.exists():
            return

        app.setStyleSheet(theme_file.read_text(encoding="utf-8"))