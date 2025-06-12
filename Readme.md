------

# 🧵 Modi App

Aplicación de escritorio para la gestión de órdenes de productos textiles.

## 📁 Estructura del Proyecto

```
modi-app/
├── assets/                   # Recursos estáticos (SVG, íconos, logos)
│   ├── icons/
│   ├── svgs/                 # Subcarpetas por categoría: /shirt, /pants, etc.
│   └── logo.png
├── data/
│   ├── database.py           # Conexión a SQLite y queries
│   └── models.py             # Clases Pydantic/SQLModel para órdenes
├── screens/                  # Pantallas de la aplicación
│   ├── __init__.py
│   ├── base_screen.py        # Clase base para pantallas
│   ├── dashboard.py          # Listado de órdenes con búsqueda
│   ├── order/
│   │   ├── create.py         # Pantalla de creación
│   │   ├── edit.py           # Edición de orden
│   │   └── view.py           # Vista detallada (para PDF)
│   └── components/           # Componentes reutilizables
│       ├── header.py         # Encabezado con logo y botón "Atrás"
│       ├── order_card.py     # Tarjeta de orden para el dashboard
│       └── pdf_exporter.py   # Lógica de generación de PDF
├── utils/
│   ├── helpers.py            # Funciones auxiliares (solo si necesario)
│   └── constants.py          # Constantes (colores, rutas)
├── main.py                   # Punto de entrada
└── requirements.txt          # Dependencias
```

## 🛠️ Tecnologías y Librerías

* **Python**
* **FPDF2**
* **PySide6**
* **pyinstaller**
* **SQLite3**

## 🧪 Instalación

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Permitir scripts de PowerShell

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## ▶️ Ejecutar la aplicación

### 1. Activar entorno virtual
Cambiar por backslash

```powershell
./venv/Scripts/Activate.ps1
```

### 2. Ejecutar la app

```bash
python modiapp/main.py
```

---

## 📜 Licencia y Créditos

Desarrollado por **ElDanissito**  
Contribuciones por **LJuandalZPH**  
Licencia: MIT

---
