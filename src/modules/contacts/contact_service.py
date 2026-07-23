"""Reglas de negocio para contactos."""

from src.modules.contacts.contact_repository import ContactRepository


class ContactService:
    """Valida y registra clientes o proveedores."""

    def __init__(self, repository: ContactRepository) -> None:
        self._repository = repository

    def list_contacts(self) -> list[dict[str, object]]:
        return sorted(
            self._repository.load(), key=lambda contact: str(contact["Nombre"]).lower()
        )

    def add_contact(self, document: str, name: str, phone: str, email: str) -> None:
        document, name = document.strip(), name.strip()
        if not document or not name:
            raise ValueError("El documento y el nombre son obligatorios.")
        contacts = self._repository.load()
        if any(str(contact["Documento"]).strip() == document for contact in contacts):
            raise ValueError("Ya existe un contacto con ese documento.")
        contacts.append(
            {
                "Documento": document,
                "Nombre": name,
                "Teléfono": phone.strip(),
                "Correo": email.strip(),
            }
        )
        self._repository.save(contacts)
