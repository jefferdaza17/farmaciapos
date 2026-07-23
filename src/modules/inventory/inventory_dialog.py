"""Diálogo para registrar medicamentos."""

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QLineEdit,
    QSpinBox,
)


class InventoryDialog(QDialog):
    """Solicita la información de un medicamento nuevo."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Nuevo medicamento")
        self.setMinimumWidth(380)

        self.code_input = QLineEdit()
        self.name_input = QLineEdit()
        self.laboratory_input = QLineEdit()
        self.price_input = QDoubleSpinBox()
        self.price_input.setRange(0, 99_999_999)
        self.price_input.setDecimals(2)
        self.price_input.setPrefix("$ ")
        self.stock_input = QSpinBox()
        self.stock_input.setRange(0, 9_999_999)
        self.minimum_stock_input = QSpinBox()
        self.minimum_stock_input.setRange(0, 9_999_999)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QFormLayout(self)
        layout.addRow("Código *", self.code_input)
        layout.addRow("Nombre *", self.name_input)
        layout.addRow("Laboratorio", self.laboratory_input)
        layout.addRow("Precio", self.price_input)
        layout.addRow("Stock inicial", self.stock_input)
        layout.addRow("Stock mínimo", self.minimum_stock_input)
        layout.addRow(buttons)
