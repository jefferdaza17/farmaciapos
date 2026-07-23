"""Dashboard principal de FarmaciaPOS."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.core.theme_manager import ThemeManager
from src.modules.reports.report_service import ReportService


class HomePage(QWidget):
    """Presenta un resumen visual de la operación de la farmacia."""

    def __init__(self, report_service: ReportService | None = None) -> None:
        super().__init__()
        self._report_service = report_service or ReportService()
        self._initialize_ui()
        self.refresh()

    def refresh(self) -> None:
        """Actualiza los indicadores mostrados en el dashboard."""
        summary = self._report_service.summary()
        self._metrics["Medicamentos"].setText(str(summary["Medicamentos registrados"]))
        self._metrics["Unidades"].setText(str(summary["Unidades en inventario"]))
        self._metrics["Stock bajo"].setText(str(summary["Productos con stock bajo"]))
        self._metrics["Ventas"].setText(f"${float(summary['Total vendido']):,.2f}")

    def _initialize_ui(self) -> None:
        title = QLabel("Buenos días")
        title.setStyleSheet(
            f"font-size: 28px; font-weight: 700; color: {ThemeManager.TEXT_PRIMARY};"
        )
        subtitle = QLabel("Aquí tienes un resumen de la operación de tu farmacia.")
        subtitle.setStyleSheet(
            f"font-size: 15px; color: {ThemeManager.TEXT_SECONDARY};"
        )

        self._metrics: dict[str, QLabel] = {}
        metrics_layout = QGridLayout()
        metrics_layout.setHorizontalSpacing(16)
        metrics_layout.setVerticalSpacing(16)
        card_specs = (
            ("Medicamentos", "Productos registrados", ThemeManager.PRIMARY_COLOR),
            ("Unidades", "Unidades disponibles", ThemeManager.SUCCESS_COLOR),
            ("Stock bajo", "Requieren reposición", ThemeManager.WARNING_COLOR),
            ("Ventas", "Ventas acumuladas", ThemeManager.PURPLE_COLOR),
        )
        for position, (key, description, color) in enumerate(card_specs):
            card = QFrame()
            card.setObjectName("metricCard")
            card.setStyleSheet(
                f"QFrame#metricCard {{ background: {ThemeManager.SURFACE_COLOR}; "
                f"border: 1px solid {ThemeManager.BORDER_COLOR}; border-radius: 12px; }}"
            )
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(20, 18, 20, 18)
            accent = QLabel(key)
            accent.setStyleSheet(f"font-size: 13px; font-weight: 700; color: {color};")
            value_label = QLabel("0")
            value_label.setStyleSheet("font-size: 26px; font-weight: 700;")
            description_label = QLabel(description)
            description_label.setStyleSheet(f"color: {ThemeManager.TEXT_SECONDARY};")
            card_layout.addWidget(accent)
            card_layout.addWidget(value_label)
            card_layout.addWidget(description_label)
            self._metrics[key] = value_label
            metrics_layout.addWidget(card, position // 2, position % 2)

        activity = QFrame()
        activity.setObjectName("activityCard")
        activity.setStyleSheet(
            f"QFrame#activityCard {{ background: {ThemeManager.SURFACE_COLOR}; "
            f"border: 1px solid {ThemeManager.BORDER_COLOR}; border-radius: 12px; }}"
        )
        activity_layout = QVBoxLayout(activity)
        activity_layout.setContentsMargins(22, 20, 22, 20)
        activity_title = QLabel("Resumen de la operación")
        activity_title.setStyleSheet("font-size: 16px; font-weight: 700;")
        activity_text = QLabel(
            "Usa el módulo Reportes para revisar ventas, compras y medicamentos que requieren reposición."
        )
        activity_text.setWordWrap(True)
        activity_text.setStyleSheet(f"color: {ThemeManager.TEXT_SECONDARY};")
        activity_layout.addWidget(activity_title)
        activity_layout.addWidget(activity_text)

        refresh_button = QPushButton("Actualizar indicadores")
        refresh_button.clicked.connect(self.refresh)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(10)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(18)
        layout.addLayout(metrics_layout)
        layout.addSpacing(8)
        layout.addWidget(activity)
        layout.addWidget(refresh_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addStretch()
