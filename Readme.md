# Ferdinand - Sistema de Gestión de Órdenes

Sistema de gestión de órdenes para la sastrería Ferdinand.

## Requisitos

- Python 3.8 o superior
- PySide6
- PyInstaller (para crear el ejecutable)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/ferdinand.git
cd ferdinand
```

2. Crear un entorno virtual:
```bash
python -m venv venv
```

3. Activar el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

### Modo Desarrollo

Para ejecutar la aplicación en modo desarrollo:

```bash
python modiapp/main.py
```

### Crear Ejecutable

Para crear un ejecutable de la aplicación:

```bash
pyinstaller modiapp.spec
```

El ejecutable se creará en la carpeta `dist`.

## Estructura del Proyecto

```
ferdinand/
├── modiapp/
│   ├── assets/         # Imágenes y recursos
│   ├── screens/        # Pantallas de la aplicación
│   ├── database.py     # Módulo de base de datos
│   └── main.py         # Punto de entrada
├── docs/
│   └── svgs/          # Archivos SVG para los modelos
├── data/              # Base de datos SQLite
├── requirements.txt   # Dependencias
└── modiapp.spec      # Configuración de PyInstaller
```

## Características

- Gestión de órdenes de sastrería
- Medidas para camisas, sacos y pantalones
- Selección de modelos con visualización SVG
- Sistema de referencias y valores
- Base de datos SQLite para persistencia
- Interfaz gráfica moderna y fácil de usar

## Base de Datos

La aplicación utiliza SQLite como base de datos. Los datos se almacenan en el archivo `data/orders.db`. La estructura incluye:

- Tabla `orders`: Información principal de las órdenes
- Tabla `order_details`: Detalles y medidas de cada orden
- Tabla `order_references`: Referencias y valores de cada orden

## Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

Desarrollado por **ElDanissito**  
Contribuciones por **LJuandalZPH**  
Licencia: MIT

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
