"""Pantalla para crear ventas."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from src.core.theme_manager import ThemeManager
from src.modules.sales.sales_service import SalesService


class SalesPage(QWidget):
    """Permite armar y confirmar una venta."""

    def __init__(self, service: SalesService | None = None) -> None:
        super().__init__()
        self._service = service or SalesService()
        self._items: list[dict[str, object]] = []
        self._initialize_ui()

    def _initialize_ui(self) -> None:
        title = QLabel("Ventas")
        title.setStyleSheet(
            f"font-size: {ThemeManager.FONT_SIZE_TITLE}px; font-weight: 700;"
        )
        subtitle = QLabel("Agregue medicamentos por código y confirme la venta.")
        subtitle.setStyleSheet(f"color: {ThemeManager.TEXT_SECONDARY};")

        self._code_input = QLineEdit()
        self._code_input.setPlaceholderText("Código del medicamento")
        self._code_input.returnPressed.connect(self._add_item)
        self._quantity_input = QSpinBox()
        self._quantity_input.setRange(1, 9_999_999)
        add_button = QPushButton("Agregar")
        add_button.clicked.connect(self._add_item)

        product_card = QFrame()
        product_card.setObjectName("salesProductCard")
        product_card.setStyleSheet(
            f"QFrame#salesProductCard {{ background: white; "
            f"border: 1px solid {ThemeManager.BORDER_COLOR}; border-radius: 10px; }}"
        )
        product_bar = QHBoxLayout(product_card)
        product_bar.setContentsMargins(16, 12, 16, 12)
        product_bar.addWidget(self._code_input, 1)
        product_bar.addWidget(QLabel("Cantidad"))
        product_bar.addWidget(self._quantity_input)
        product_bar.addWidget(add_button)

        self._table = QTableWidget(0, 5)
        self._table.setHorizontalHeaderLabels(
            ("Código", "Producto", "Cantidad", "Precio", "Subtotal")
        )
        self._table.horizontalHeader().setStretchLastSection(True)
        self._table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self._table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._table.verticalHeader().setVisible(False)

        self._total_label = QLabel("$0.00")
        self._total_label.setStyleSheet(
            f"font-size: 26px; font-weight: 700; color: {ThemeManager.PRIMARY_COLOR};"
        )
        total_caption = QLabel("Total de la venta")
        total_caption.setStyleSheet(f"color: {ThemeManager.TEXT_SECONDARY};")
        total_box = QVBoxLayout()
        total_box.setSpacing(0)
        total_box.addWidget(total_caption)
        total_box.addWidget(self._total_label)
        remove_button = QPushButton("Quitar seleccionado")
        remove_button.clicked.connect(self._remove_selected)
        confirm_button = QPushButton("Confirmar venta")
        confirm_button.clicked.connect(self._confirm_sale)
        footer = QHBoxLayout()
        footer.addLayout(total_box)
        footer.addStretch()
        footer.addWidget(remove_button)
        footer.addWidget(confirm_button)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(12)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(product_card)
        layout.addWidget(self._table, 1)
        layout.addLayout(footer)

    def _add_item(self) -> None:
        try:
            item = self._service.create_item(
                self._code_input.text(), self._quantity_input.value()
            )
        except ValueError as error:
            QMessageBox.warning(self, "No se pudo agregar", str(error))
            return

        for existing_item in self._items:
            if existing_item["Código"] == item["Código"]:
                existing_item["Cantidad"] = int(existing_item["Cantidad"]) + int(
                    item["Cantidad"]
                )
                existing_item["Subtotal"] = round(
                    float(existing_item["Precio"]) * int(existing_item["Cantidad"]), 2
                )
                self._refresh_table()
                self._code_input.clear()
                return

        self._items.append(item)
        self._refresh_table()
        self._code_input.clear()

    def _remove_selected(self) -> None:
        row = self._table.currentRow()
        if row >= 0:
            self._items.pop(row)
            self._refresh_table()

    def _confirm_sale(self) -> None:
        try:
            receipt = self._service.confirm_sale(self._items)
        except ValueError as error:
            QMessageBox.warning(self, "No se pudo confirmar", str(error))
            return

        QMessageBox.information(
            self,
            "Venta registrada",
            f"Venta registrada correctamente. Factura: {receipt}",
        )
        self._items.clear()
        self._refresh_table()

    def _refresh_table(self) -> None:
        self._table.setRowCount(len(self._items))
        for row, item in enumerate(self._items):
            values = (
                str(item["Código"]),
                str(item["Nombre"]),
                str(item["Cantidad"]),
                f"${float(item['Precio']):,.2f}",
                f"${float(item['Subtotal']):,.2f}",
            )
            for column, value in enumerate(values):
                table_item = QTableWidgetItem(value)
                if column in {2, 3, 4}:
                    table_item.setTextAlignment(
                        int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                    )
                self._table.setItem(row, column, table_item)
        total = sum(float(item["Subtotal"]) for item in self._items)
        self._total_label.setText(f"${total:,.2f}")
