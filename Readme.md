# ModiApp - Sistema de Gestión de Órdenes de Modistería

## Descripción
ModiApp es una aplicación de escritorio desarrollada en Python con PySide6 para la gestión integral de órdenes de modistería. Permite crear, gestionar y visualizar órdenes de trabajo con especificaciones detalladas para camisas, sacos y pantalones.

## Características Principales

### 🎨 **Interfaz Moderna con Modo Claro**
- **Tema claro por defecto**: Interfaz limpia y profesional con colores modernos
- **Diseño responsivo**: Adaptable a diferentes tamaños de pantalla
- **Efectos visuales**: Transiciones suaves y efectos hover para mejor UX
- **Iconografía**: Botones con iconos intuitivos para mejor usabilidad

### 📊 **Dashboard Principal**
- Vista general de todas las órdenes
- Filtros avanzados por estado, fecha y cliente
- Tabla con información financiera y estados visuales
- Botones de acción con colores diferenciados:
  - 📥 **Descargar** (Azul)
  - 🔄 **Cambiar Estado** (Naranja)
  - 👁 **Ver** (Gris)
  - 🗑 **Eliminar** (Rojo)

### ✏️ **Creación de Órdenes**
- **Sección de Camisa**: Medidas, modelos de espalda, bolsillos, puños y cuellos
- **Sección de Saco**: Medidas, estilos, solapas, bolsillos y chalecos
- **Sección de Pantalón**: Medidas, bolsillos, pretinas y acabados
- **Información Financiera**: Valor, abono y cálculo automático de saldo
- **Referencias**: Gestión de telas y materiales

### 👁️ **Visualización de Órdenes**
- Vista detallada de cada orden
- Visualización de modelos con imágenes SVG
- Información financiera con códigos de color
- Estados visuales diferenciados

## Tecnologías Utilizadas

- **Python 3.8+**
- **PySide6**: Framework de interfaz gráfica
- **SQLite**: Base de datos local
- **FPDF**: Generación de reportes PDF
- **CSS**: Estilos personalizados para la interfaz

## Instalación y Configuración

### Requisitos Previos
```bash
Python 3.8 o superior
pip (gestor de paquetes de Python)
```

### Instalación
1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd ModiApp
```

2. Crear entorno virtual:
```bash
python -m venv venv
```

3. Activar entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

5. Ejecutar la aplicación:
```bash
python main.py
```

## Estructura del Proyecto

```
ModiApp/
├── main.py                 # Punto de entrada principal
├── modiapp/
│   ├── __init__.py
│   ├── main.py            # Configuración de la aplicación
│   ├── database.py        # Gestión de base de datos
│   ├── styles.py          # Estilos CSS del modo claro
│   ├── assets/            # Recursos (logo, iconos)
│   ├── data/              # Base de datos SQLite
│   └── screens/           # Pantallas de la aplicación
│       ├── __init__.py
│       ├── dashboard_screen.py      # Dashboard principal
│       ├── create_order_screen.py   # Creación de órdenes
│       └── view_order_screen.py     # Visualización de órdenes
├── docs/                  # Documentación y recursos SVG
│   └── svgs/             # Imágenes SVG de modelos
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## Características del Modo Claro

### 🎨 **Paleta de Colores**
- **Primario**: Azul (#2563eb) - Botones principales y elementos de acción
- **Secundario**: Gris (#64748b) - Elementos secundarios
- **Éxito**: Verde (#059669) - Estados positivos y valores monetarios
- **Advertencia**: Naranja (#d97706) - Estados pendientes
- **Peligro**: Rojo (#dc2626) - Acciones destructivas y saldos negativos

### 🎯 **Mejoras de UX**
- **Efectos hover**: Transiciones suaves en botones y elementos interactivos
- **Estados visuales**: Colores diferenciados para estados de órdenes
- **Información financiera**: Códigos de color para valores monetarios
- **Navegación intuitiva**: Botones con iconos y texto descriptivo
- **Formularios mejorados**: Placeholders y validación visual

### 📱 **Responsividad**
- **Layout adaptable**: Se ajusta a diferentes tamaños de ventana
- **Scroll inteligente**: Áreas de desplazamiento optimizadas
- **Grid system**: Organización eficiente de elementos

## Funcionalidades por Pantalla

### Dashboard
- ✅ Lista de órdenes con información completa
- ✅ Filtros por estado, fecha y cliente
- ✅ Acciones rápidas (descargar, cambiar estado, ver, eliminar)
- ✅ Información financiera con códigos de color
- ✅ Estados visuales diferenciados

### Crear Orden
- ✅ Formulario completo para camisa, saco y pantalón
- ✅ Selección visual de modelos con imágenes SVG
- ✅ Cálculo automático de saldo
- ✅ Gestión de referencias y materiales
- ✅ Validación de campos

### Ver Orden
- ✅ Vista detallada de la orden completa
- ✅ Visualización de modelos seleccionados
- ✅ Información financiera destacada
- ✅ Estados visuales claros

## Base de Datos

La aplicación utiliza SQLite para almacenar:
- **Órdenes**: Información principal de cada orden
- **Detalles**: Especificaciones técnicas de cada prenda
- **Referencias**: Materiales y telas utilizadas

## Generación de Reportes

- **Formato PDF**: Reportes profesionales con logo de la empresa
- **Información completa**: Incluye medidas, modelos y especificaciones
- **Diseño optimizado**: Formato Letter con márgenes reducidos

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Soporte

Para soporte técnico o consultas sobre el proyecto, contactar a través de:
- Email: [tu-email@ejemplo.com]
- Issues: [GitHub Issues]

---

**Desarrollado con ❤️ para la industria de la modistería**
