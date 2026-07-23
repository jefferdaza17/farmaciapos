"""Pantalla de proveedores."""

from src.modules.contacts.contact_page import ContactPage
from src.modules.contacts.contact_repository import ContactRepository
from src.modules.contacts.contact_service import ContactService


class SuppliersPage(ContactPage):
    """Administra los proveedores de la farmacia."""

    def __init__(self) -> None:
        super().__init__(
            "Proveedores", ContactService(ContactRepository("Proveedores"))
        )
