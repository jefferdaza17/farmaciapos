"""Pantalla de reportes básicos."""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from src.core.theme_manager import ThemeManager
from src.modules.reports.report_service import ReportService


class ReportsPage(QWidget):
    """Muestra indicadores y alertas de stock bajo."""

    def __init__(self, service: ReportService | None = None) -> None:
        super().__init__()
        self._service = service or ReportService()
        self._initialize_ui()
        self.refresh()

    def refresh(self) -> None:
        """Actualiza los datos presentados desde el archivo de operación."""
        summary = self._service.summary()
        self._summary_table.setRowCount(len(summary))
        for row, (label, value) in enumerate(summary.items()):
            if "Total" in label:
                value = f"${float(value):,.2f}"
            self._summary_table.setItem(row, 0, QTableWidgetItem(label))
            self._summary_table.setItem(row, 1, QTableWidgetItem(str(value)))
        low_stock = self._service.low_stock()
        self._low_stock_table.setRowCount(len(low_stock))
        for row, item in enumerate(low_stock):
            for column, header in enumerate(
                ("Código", "Nombre", "Stock", "Stock mínimo")
            ):
                self._low_stock_table.setItem(
                    row, column, QTableWidgetItem(str(item[header]))
                )

    def _initialize_ui(self) -> None:
        title = QLabel("Reportes")
        title.setStyleSheet(
            f"font-size: {ThemeManager.FONT_SIZE_TITLE}px; font-weight: 700;"
        )
        refresh_button = QPushButton("Actualizar")
        refresh_button.clicked.connect(self.refresh)
        header = QHBoxLayout()
        header.addWidget(title)
        header.addStretch()
        header.addWidget(refresh_button)
        summary_label = QLabel("Resumen operativo")
        summary_label.setStyleSheet("font-size: 16px; font-weight: 700;")
        self._summary_table = QTableWidget(0, 2)
        self._summary_table.setHorizontalHeaderLabels(("Indicador", "Valor"))
        self._summary_table.horizontalHeader().setStretchLastSection(True)
        self._summary_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._summary_table.verticalHeader().setVisible(False)
        low_stock_label = QLabel("Productos con stock bajo")
        low_stock_label.setStyleSheet("font-size: 16px; font-weight: 700;")
        self._low_stock_table = QTableWidget(0, 4)
        self._low_stock_table.setHorizontalHeaderLabels(
            ("Código", "Nombre", "Stock", "Stock mínimo")
        )
        self._low_stock_table.horizontalHeader().setStretchLastSection(True)
        self._low_stock_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._low_stock_table.verticalHeader().setVisible(False)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.addLayout(header)
        layout.addWidget(summary_label)
        layout.addWidget(self._summary_table)
        layout.addWidget(low_stock_label)
        layout.addWidget(self._low_stock_table, 1)
