"""Pantalla de clientes."""

from src.modules.contacts.contact_page import ContactPage
from src.modules.contacts.contact_repository import ContactRepository
from src.modules.contacts.contact_service import ContactService


class ClientsPage(ContactPage):
    """Administra los clientes de la farmacia."""

    def __init__(self) -> None:
        super().__init__("Clientes", ContactService(ContactRepository("Clientes")))
