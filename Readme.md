La estructura recomendada par el proyecto es:

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