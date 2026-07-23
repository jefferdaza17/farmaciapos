"""Prueba del flujo principal del MVP sin interfaz gráfica."""

from pathlib import Path

from src.modules.contacts.contact_repository import ContactRepository
from src.modules.contacts.contact_service import ContactService
from src.modules.inventory.inventory_repository import InventoryRepository
from src.modules.inventory.inventory_service import InventoryService
from src.modules.purchases.purchase_repository import PurchaseRepository
from src.modules.purchases.purchase_service import PurchaseService
from src.modules.reports.report_service import ReportService
from src.modules.sales.sales_repository import SalesRepository
from src.modules.sales.sales_service import SalesService


def test_mvp_operational_flow(tmp_path: Path) -> None:
    """Registra contactos, compra, venta y valida los indicadores finales."""
    file_path = tmp_path / "farmacia.xlsx"
    inventory = InventoryService(InventoryRepository(file_path))
    inventory.add_medication("MED-001", "Acetaminofén", "Genfar", 2500, 10, 3)

    ContactService(ContactRepository("Clientes", file_path)).add_contact(
        "1001", "Ana Pérez", "3000000000", "ana@example.com"
    )
    ContactService(ContactRepository("Proveedores", file_path)).add_contact(
        "9001", "Distribuidora Salud", "3100000000", "ventas@example.com"
    )

    purchases = PurchaseService(inventory, PurchaseRepository(file_path))
    purchases.register_purchase("Distribuidora Salud", "MED-001", 5, 1800)

    sales = SalesService(inventory, SalesRepository(file_path))
    sales.confirm_sale([sales.create_item("MED-001", 3)])

    assert inventory.medication_by_code("MED-001")["Stock"] == 12
    summary = ReportService(inventory, file_path).summary()
    assert summary["Ventas registradas"] == 1
    assert summary["Compras registradas"] == 1
    assert summary["Total vendido"] == 7500.0
    assert summary["Total comprado"] == 9000.0
