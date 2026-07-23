"""Reglas de negocio del inventario."""

from src.modules.inventory.inventory_repository import InventoryRepository


class InventoryService:
    """Valida y administra los medicamentos del inventario."""

    def __init__(self, repository: InventoryRepository | None = None) -> None:
        self._repository = repository or InventoryRepository()

    def list_medications(self) -> list[dict[str, object]]:
        """Obtiene los medicamentos ordenados por nombre."""
        return sorted(
            self._repository.load(),
            key=lambda medication: str(medication["Nombre"]).lower(),
        )

    def add_medication(
        self,
        code: str,
        name: str,
        laboratory: str,
        price: float,
        stock: int,
        minimum_stock: int,
    ) -> None:
        """Valida y registra un medicamento nuevo."""
        code, name, laboratory = code.strip(), name.strip(), laboratory.strip()
        if not code or not name:
            raise ValueError("El código y el nombre son obligatorios.")
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0 or minimum_stock < 0:
            raise ValueError("Las cantidades de stock no pueden ser negativas.")

        medications = self._repository.load()
        if any(
            str(item["Código"]).strip().lower() == code.lower() for item in medications
        ):
            raise ValueError("Ya existe un medicamento con ese código.")

        medications.append(
            {
                "Código": code,
                "Nombre": name,
                "Laboratorio": laboratory,
                "Precio": round(price, 2),
                "Stock": stock,
                "Stock mínimo": minimum_stock,
            }
        )
        self._repository.save(medications)

    def medication_by_code(self, code: str) -> dict[str, object]:
        """Busca un medicamento por su código."""
        normalized_code = code.strip().lower()
        for medication in self._repository.load():
            if str(medication["Código"]).strip().lower() == normalized_code:
                return medication
        raise ValueError("No se encontró un medicamento con ese código.")

    def deduct_stock(self, items: list[dict[str, object]]) -> None:
        """Descuenta existencias después de validar toda una venta."""
        medications = self._repository.load()
        medications_by_code = {
            str(medication["Código"]).strip().lower(): medication
            for medication in medications
        }

        for item in items:
            code = str(item["Código"]).strip().lower()
            quantity = int(item["Cantidad"])
            medication = medications_by_code.get(code)
            if medication is None:
                raise ValueError(f"El medicamento {item['Código']} ya no existe.")
            if quantity <= 0:
                raise ValueError("La cantidad debe ser mayor que cero.")
            if int(medication["Stock"]) < quantity:
                raise ValueError(
                    f"Stock insuficiente para {medication['Nombre']}. "
                    f"Disponible: {medication['Stock']}."
                )

        for item in items:
            medication = medications_by_code[str(item["Código"]).strip().lower()]
            medication["Stock"] = int(medication["Stock"]) - int(item["Cantidad"])
        self._repository.save(medications)

    def add_stock(self, code: str, quantity: int) -> None:
        """Aumenta las existencias de un medicamento registrado."""
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        medications = self._repository.load()
        normalized_code = code.strip().lower()
        for medication in medications:
            if str(medication["Código"]).strip().lower() == normalized_code:
                medication["Stock"] = int(medication["Stock"]) + quantity
                self._repository.save(medications)
                return
        raise ValueError("No se encontró un medicamento con ese código.")
