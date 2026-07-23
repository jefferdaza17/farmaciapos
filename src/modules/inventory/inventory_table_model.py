"""Modelo Qt para la tabla de medicamentos."""

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QColor


class InventoryTableModel(QAbstractTableModel):
    """Expone los datos del inventario a un ``QTableView``."""

    HEADERS = ("Código", "Nombre", "Laboratorio", "Precio", "Stock", "Stock mínimo")

    def __init__(self, medications: list[dict[str, object]] | None = None) -> None:
        super().__init__()
        self._medications = medications or []

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._medications)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self.HEADERS)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):  # type: ignore[override]
        if not index.isValid():
            return None
        medication = self._medications[index.row()]
        header = self.HEADERS[index.column()]
        value = medication[header]

        if role == Qt.ItemDataRole.DisplayRole:
            if header == "Precio":
                return f"${float(value):,.2f}"
            return str(value)
        if role == Qt.ItemDataRole.TextAlignmentRole and header in {
            "Precio",
            "Stock",
            "Stock mínimo",
        }:
            return int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        if role == Qt.ItemDataRole.ForegroundRole and header == "Stock":
            if int(value) <= int(medication["Stock mínimo"]):
                return QColor("#DC2626")
        return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):  # noqa: N802
        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
        ):
            return self.HEADERS[section]
        return None

    def set_medications(self, medications: list[dict[str, object]]) -> None:
        """Actualiza el contenido visible de la tabla."""
        self.beginResetModel()
        self._medications = medications
        self.endResetModel()
