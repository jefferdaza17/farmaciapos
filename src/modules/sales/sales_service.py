"""Reglas de negocio para el registro de ventas."""

from datetime import datetime

from src.modules.inventory.inventory_service import InventoryService
from src.modules.sales.sales_repository import SalesRepository


class SalesService:
    """Prepara productos y confirma ventas contra el inventario."""

    def __init__(
        self,
        inventory_service: InventoryService | None = None,
        repository: SalesRepository | None = None,
    ) -> None:
        self._inventory_service = inventory_service or InventoryService()
        self._repository = repository or SalesRepository()

    def create_item(self, code: str, quantity: int) -> dict[str, object]:
        """Construye una línea de venta a partir del código del medicamento."""
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        medication = self._inventory_service.medication_by_code(code)
        if int(medication["Stock"]) < quantity:
            raise ValueError(
                f"Stock insuficiente para {medication['Nombre']}. "
                f"Disponible: {medication['Stock']}."
            )
        price = float(medication["Precio"])
        return {
            "Código": medication["Código"],
            "Nombre": medication["Nombre"],
            "Cantidad": quantity,
            "Precio": price,
            "Subtotal": round(price * quantity, 2),
        }

    def confirm_sale(self, items: list[dict[str, object]]) -> str:
        """Descuenta existencias y registra una venta confirmada."""
        if not items:
            raise ValueError("Agregue al menos un producto a la venta.")

        now = datetime.now()
        receipt = now.strftime("V%Y%m%d%H%M%S%f")
        self._inventory_service.deduct_stock(items)
        self._repository.save_sale(receipt, now.isoformat(timespec="seconds"), items)
        return receipt
