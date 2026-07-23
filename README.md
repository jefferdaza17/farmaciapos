# FarmaciaPOS

Aplicación de escritorio para gestionar una farmacia, desarrollada con Python y PySide6.

## Requisitos

- Python 3.13 o posterior.

## Instalación y ejecución

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
python -m src.main
```

## Estado actual

- Navegación entre Inicio e Inventario.
- Consulta y búsqueda de medicamentos.
- Registro de medicamentos con validación de código, precio y stock.
- Persistencia local en `data/excel/farmacia.xlsx`. El archivo se crea automáticamente en el primer inicio y no se versiona, porque contiene datos de operación local.
- Ventas por código de medicamento, con cálculo de total, verificación de existencias y descuento automático del stock.
- Clientes y proveedores con registro independiente.
- Compras que incrementan existencias y se registran como movimiento.
- Dashboard y reportes básicos de operación, ventas, compras y alertas de stock bajo.

## Alcance del MVP

El MVP permite administrar inventario, clientes, proveedores, compras y ventas con persistencia local en Excel. No incluye facturación electrónica, impuestos configurables, control de vencimientos, autenticación ni sincronización multiusuario.
