from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Sidebar(QWidget):
    """Panel lateral de navegación."""

    def __init__(self) -> None:
        super().__init__()
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setFixedWidth(260)
        self.setObjectName("sidebar")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        logo = QLabel("💊")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setObjectName("logo")

        title = QLabel("FarmaciaPOS")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName("sidebarTitle")

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addStretch()