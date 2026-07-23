"""Reglas de negocio para compras."""

from datetime import datetime

from src.modules.inventory.inventory_service import InventoryService
from src.modules.purchases.purchase_repository import PurchaseRepository


class PurchaseService:
    """Registra entradas y actualiza existencias."""

    def __init__(
        self,
        inventory_service: InventoryService | None = None,
        repository: PurchaseRepository | None = None,
    ) -> None:
        self._inventory_service = inventory_service or InventoryService()
        self._repository = repository or PurchaseRepository()

    def register_purchase(
        self, supplier: str, code: str, quantity: int, unit_cost: float
    ) -> str:
        """Valida, registra la compra y aumenta el stock."""
        if not supplier.strip():
            raise ValueError("El proveedor es obligatorio.")
        if unit_cost < 0:
            raise ValueError("El costo unitario no puede ser negativo.")
        self._inventory_service.add_stock(code, quantity)
        now = datetime.now()
        purchase_id = now.strftime("C%Y%m%d%H%M%S%f")
        self._repository.save_purchase(
            purchase_id,
            now.isoformat(timespec="seconds"),
            supplier.strip(),
            code.strip(),
            quantity,
            unit_cost,
        )
        return purchase_id
