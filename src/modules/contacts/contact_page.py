"""Página reutilizable de clientes y proveedores."""

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from src.core.theme_manager import ThemeManager
from src.modules.contacts.contact_service import ContactService


class ContactPage(QWidget):
    """Muestra y permite crear contactos de un tipo determinado."""

    def __init__(self, title: str, service: ContactService) -> None:
        super().__init__()
        self._title = title
        self._service = service
        self._initialize_ui()
        self.refresh()

    def refresh(self) -> None:
        contacts = self._service.list_contacts()
        self._table.setRowCount(len(contacts))
        for row, contact in enumerate(contacts):
            for column, header in enumerate(
                ("Documento", "Nombre", "Teléfono", "Correo")
            ):
                self._table.setItem(row, column, QTableWidgetItem(str(contact[header])))

    def _initialize_ui(self) -> None:
        title = QLabel(self._title)
        title.setStyleSheet(
            f"font-size: {ThemeManager.FONT_SIZE_TITLE}px; font-weight: 700;"
        )
        subtitle = QLabel(f"Administre los {self._title.lower()} de la farmacia.")
        subtitle.setStyleSheet(f"color: {ThemeManager.TEXT_SECONDARY};")
        add_button = QPushButton(f"+ Nuevo {self._title[:-1].lower()}")
        add_button.clicked.connect(self._show_new_contact_dialog)
        toolbar = QHBoxLayout()
        toolbar.addStretch()
        toolbar.addWidget(add_button)
        self._table = QTableWidget(0, 4)
        self._table.setHorizontalHeaderLabels(
            ("Documento", "Nombre", "Teléfono", "Correo")
        )
        self._table.horizontalHeader().setStretchLastSection(True)
        self._table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._table.verticalHeader().setVisible(False)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(toolbar)
        layout.addWidget(self._table, 1)

    def _show_new_contact_dialog(self) -> None:
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Nuevo {self._title[:-1].lower()}")
        document, name, phone, email = (
            QLineEdit(),
            QLineEdit(),
            QLineEdit(),
            QLineEdit(),
        )
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout = QFormLayout(dialog)
        layout.addRow("Documento *", document)
        layout.addRow("Nombre *", name)
        layout.addRow("Teléfono", phone)
        layout.addRow("Correo", email)
        layout.addRow(buttons)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        try:
            self._service.add_contact(
                document.text(), name.text(), phone.text(), email.text()
            )
        except ValueError as error:
            QMessageBox.warning(self, "No se pudo registrar", str(error))
            return
        self.refresh()
