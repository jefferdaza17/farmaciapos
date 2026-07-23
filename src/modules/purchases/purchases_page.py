"""Pantalla para registrar compras unitarias."""

from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from src.core.theme_manager import ThemeManager
from src.modules.purchases.purchase_service import PurchaseService


class PurchasesPage(QWidget):
    """Registra entradas de medicamentos que ya están en inventario."""

    def __init__(self, service: PurchaseService | None = None) -> None:
        super().__init__()
        self._service = service or PurchaseService()
        self._initialize_ui()

    def _initialize_ui(self) -> None:
        title = QLabel("Compras")
        title.setStyleSheet(
            f"font-size: {ThemeManager.FONT_SIZE_TITLE}px; font-weight: 700;"
        )
        subtitle = QLabel(
            "Registre una entrada para aumentar el stock de un medicamento existente."
        )
        subtitle.setStyleSheet(f"color: {ThemeManager.TEXT_SECONDARY};")
        self._supplier_input = QLineEdit()
        self._code_input = QLineEdit()
        self._quantity_input = QSpinBox()
        self._quantity_input.setRange(1, 9_999_999)
        self._cost_input = QDoubleSpinBox()
        self._cost_input.setRange(0, 99_999_999)
        self._cost_input.setDecimals(2)
        self._cost_input.setPrefix("$ ")
        save_button = QPushButton("Registrar compra")
        save_button.clicked.connect(self._register_purchase)
        form = QFormLayout()
        form.addRow("Proveedor *", self._supplier_input)
        form.addRow("Código del medicamento *", self._code_input)
        form.addRow("Cantidad *", self._quantity_input)
        form.addRow("Costo unitario", self._cost_input)
        actions = QHBoxLayout()
        actions.addStretch()
        actions.addWidget(save_button)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(16)
        layout.addLayout(form)
        layout.addLayout(actions)
        layout.addStretch()

    def _register_purchase(self) -> None:
        try:
            purchase_id = self._service.register_purchase(
                self._supplier_input.text(),
                self._code_input.text(),
                self._quantity_input.value(),
                self._cost_input.value(),
            )
        except ValueError as error:
            QMessageBox.warning(self, "No se pudo registrar", str(error))
            return
        QMessageBox.information(
            self, "Compra registrada", f"Compra registrada correctamente: {purchase_id}"
        )
        self._code_input.clear()
        self._quantity_input.setValue(1)
        self._cost_input.setValue(0)
