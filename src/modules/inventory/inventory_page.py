"""Pantalla principal del módulo de inventario."""

from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from src.core.theme_manager import ThemeManager
from src.modules.inventory.inventory_dialog import InventoryDialog
from src.modules.inventory.inventory_service import InventoryService
from src.modules.inventory.inventory_table_model import InventoryTableModel


class InventoryPage(QWidget):
    """Permite consultar y registrar medicamentos."""

    def __init__(self, service: InventoryService | None = None) -> None:
        super().__init__()
        self._service = service or InventoryService()
        self._model = InventoryTableModel()
        self._proxy_model = QSortFilterProxyModel(self)
        self._proxy_model.setSourceModel(self._model)
        self._proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._proxy_model.setFilterKeyColumn(-1)
        self._initialize_ui()
        self.refresh()

    def refresh(self) -> None:
        """Recarga el inventario desde el almacenamiento local."""
        self._model.set_medications(self._service.list_medications())

    def _initialize_ui(self) -> None:
        title = QLabel("Inventario")
        title.setStyleSheet(
            f"font-size: {ThemeManager.FONT_SIZE_TITLE}px; font-weight: 700;"
        )
        subtitle = QLabel("Consulta existencias y registra medicamentos.")
        subtitle.setStyleSheet(f"color: {ThemeManager.TEXT_SECONDARY};")
        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText(
            "Buscar por código, nombre o laboratorio..."
        )
        self._search_input.textChanged.connect(self._proxy_model.setFilterFixedString)
        add_button = QPushButton("+ Nuevo medicamento")
        add_button.clicked.connect(self._add_medication)

        toolbar = QHBoxLayout()
        toolbar.addWidget(self._search_input, 1)
        toolbar.addWidget(add_button)

        self._table = QTableView()
        self._table.setModel(self._proxy_model)
        self._table.setAlternatingRowColors(True)
        self._table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self._table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self._table.horizontalHeader().setStretchLastSection(True)
        self._table.verticalHeader().setVisible(False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(12)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(toolbar)
        layout.addWidget(self._table, 1)

    def _add_medication(self) -> None:
        dialog = InventoryDialog(self)
        if dialog.exec() != InventoryDialog.DialogCode.Accepted:
            return
        try:
            self._service.add_medication(
                dialog.code_input.text(),
                dialog.name_input.text(),
                dialog.laboratory_input.text(),
                dialog.price_input.value(),
                dialog.stock_input.value(),
                dialog.minimum_stock_input.value(),
            )
        except ValueError as error:
            QMessageBox.warning(self, "No se pudo registrar", str(error))
            return
        self.refresh()
