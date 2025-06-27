"""
Estilos CSS para la aplicación ModiApp - Modo Claro
"""

import re

def interpolate_qss(qss_string):
    """
    Procesa un string QSS para reemplazar las variables CSS por sus valores literales.
    """
    # 1. Extraer variables del bloque :root
    variables = {}
    root_match = re.search(r':root\s*\{([^}]+)\}', qss_string)
    if root_match:
        root_content = root_match.group(1)
        for line in root_content.split(';'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                variables[key.strip()] = value.strip()

    # 2. Reemplazar todas las ocurrencias de var(--variable) por su valor
    def replace_var(match):
        var_name = match.group(1).strip()
        return variables.get(var_name, 'none')

    # Eliminar el bloque :root y los comentarios
    qss_string = re.sub(r'/\*.*?\*/', '', qss_string, flags=re.DOTALL)
    qss_string = re.sub(r':root\s*\{[^}]+\}', '', qss_string)
    
    # Interpolar variables
    interpolated_qss = re.sub(r'var\((--[\w-]+)\)', replace_var, qss_string)

    return interpolated_qss.strip()

# Estilos con variables (como estaba antes)
STYLES_WITH_VARS = """
/* Variables CSS para el tema claro */
:root {
    --primary-color: #2563eb;
    --primary-hover: #1d4ed8;
    --secondary-color: #64748b;
    --success-color: #059669;
    --warning-color: #d97706;
    --danger-color: #dc2626;
    --background-color: #ffffff;
    --surface-color: #f8fafc;
    --border-color: #e2e8f0;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --text-muted: #94a3b8;
    --shadow-sm: "0 1px 2px 0 rgb(0 0 0 / 0.05)";
    --shadow-md: "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)";
    --shadow-lg: "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)";
    --radius-sm: "4px";
    --radius-md: "6px";
    --radius-lg: "8px";
}

/* Estilos generales */
QWidget {
    background-color: var(--background-color);
    color: var(--text-primary);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 9pt;
}

/* Estilos para QMainWindow y ventanas principales */
QMainWindow, QWidget#mainWindow {
    background-color: var(--background-color);
    border: none;
}

/* Estilos para QGroupBox */
QGroupBox {
    background-color: var(--surface-color);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    margin-top: 1ex;
    padding-top: 15px;
    font-weight: bold;
    color: var(--text-primary);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px 0 5px;
    color: var(--text-primary);
    font-weight: 600;
}

/* Estilos para QPushButton */
QPushButton {
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: var(--radius-sm);
    padding: 8px 16px;
    font-weight: 500;
    min-height: 20px;
}

QPushButton:hover {
    background-color: var(--primary-hover);
}

QPushButton:pressed {
    background-color: #1e40af;
}

QPushButton:disabled {
    background-color: var(--text-muted);
    color: var(--text-secondary);
}

/* Botones secundarios */
QPushButton#backButton, QPushButton.secondary {
    background-color: var(--secondary-color);
}
QPushButton#backButton:hover, QPushButton.secondary:hover {
    background-color: #475569;
}

/* Botones de éxito */
QPushButton#saveButton, QPushButton#createButton, QPushButton.success {
    background-color: var(--success-color);
}
QPushButton#saveButton:hover, QPushButton#createButton:hover, QPushButton.success:hover {
    background-color: #047857;
}

/* Botones de advertencia */
QPushButton#changeStatusButton, QPushButton.warning {
    background-color: var(--warning-color);
}
QPushButton#changeStatusButton:hover, QPushButton.warning:hover {
    background-color: #b45309;
}

/* Botones de peligro */
QPushButton#deleteButton, QPushButton#cancelButton, QPushButton.danger {
    background-color: var(--danger-color);
}
QPushButton#deleteButton:hover, QPushButton#cancelButton:hover, QPushButton.danger:hover {
    background-color: #b91c1c;
}

/* Botones pequeños para la tabla */
QPushButton.small {
    padding: 4px 8px;
    font-size: 8pt;
    min-height: 16px;
}

/* Botones para añadir/quitar referencias */
QPushButton#addReferenceButton, QPushButton#deleteReferenceButton {
    padding: 0;
    font-size: 14pt;
    font-weight: bold;
    min-height: 20px;
}

QPushButton#addReferenceButton {
    background-color: var(--success-color);
}

QPushButton#addReferenceButton:hover {
    background-color: #047857;
}

QPushButton#deleteReferenceButton {
    background-color: var(--danger-color);
}

QPushButton#deleteReferenceButton:hover {
    background-color: #b91c1c;
}

/* Estilos para QLineEdit */
QLineEdit {
    background-color: white;
    border: 2px solid #90b4e0;
    border-radius: var(--radius-sm);
    padding: 6px 8px;
    color: var(--text-primary);
    selection-background-color: var(--primary-color);
}
QLineEdit:focus {
    border-color: var(--primary-color);
    border-width: 2px;
}
QLineEdit:hover {
    border-color: #94a3b8;
    border-width: 2px;
}
QLineEdit:disabled {
    background-color: var(--surface-color);
    color: var(--text-muted);
    border-color: var(--border-color);
}

/* Estilos para QComboBox */
QComboBox {
    background-color: white;
    border: 2px solid #90b4e0;
    border-radius: var(--radius-sm);
    padding: 6px 8px;
    color: var(--text-primary);
    min-height: 20px;
}
QComboBox:hover, QComboBox:focus {
    border-color: var(--primary-color);
    border-width: 2px;
}
QComboBox::drop-down {
    border: none;
    width: 20px;
}
QComboBox::down-arrow {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid var(--text-secondary);
    margin-right: 5px;
}
QComboBox QAbstractItemView {
    background-color: white;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    selection-background-color: var(--primary-color);
    selection-color: white;
}

/* Estilos para QDateEdit */
QDateEdit {
    background-color: white;
    border: 2px solid #90b4e0;
    border-radius: var(--radius-sm);
    padding: 6px 8px;
    color: var(--text-primary);
    min-height: 20px;
}
QDateEdit:focus, QDateEdit:hover {
    border-color: var(--primary-color);
    border-width: 2px;
}
QDateEdit::drop-down {
    border: none;
    width: 20px;
}
QDateEdit::down-arrow {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid var(--text-secondary);
    margin-right: 5px;
}

/* Estilos para QTableWidget */
QTableWidget {
    background-color: white;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    gridline-color: var(--border-color);
    selection-background-color: var(--primary-color);
    selection-color: white;
    alternate-background-color: var(--surface-color);
}
QTableWidget::item {
    padding: 8px;
    border-bottom: 1px solid var(--border-color);
}
QTableWidget::item:selected {
    background-color: var(--primary-color);
    color: white;
}
QHeaderView::section {
    background-color: var(--surface-color);
    color: var(--text-primary);
    padding: 8px;
    border: none;
    border-bottom: 2px solid var(--border-color);
    font-weight: 600;
}

/* Estilos para QScrollArea */
QScrollArea {
    background-color: var(--background-color);
    border: none;
}
QScrollBar:vertical {
    background-color: var(--surface-color);
    width: 12px;
    border-radius: 6px;
}
QScrollBar::handle:vertical {
    background-color: var(--border-color);
    border-radius: 6px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background-color: var(--text-secondary);
}
QScrollBar:horizontal {
    background-color: var(--surface-color);
    height: 12px;
    border-radius: 6px;
}
QScrollBar::handle:horizontal {
    background-color: var(--border-color);
    border-radius: 6px;
    min-width: 20px;
}
QScrollBar::handle:horizontal:hover {
    background-color: var(--text-secondary);
}

/* Estilos para QLabel */
QLabel#title {
    font-size: 14pt;
    font-weight: bold;
}
QLabel#subtitle {
    font-size: 11pt;
    font-weight: 600;
    color: var(--text-secondary);
}
QLabel.muted {
    color: var(--text-muted);
}
QLabel.field-label {
    font-weight: 600;
}
QLabel.field-value {
    color: var(--text-secondary);
    padding-left: 10px;
}
QLabel.section-title {
    font-size: 12pt;
    font-weight: bold;
    color: var(--primary-color);
    margin-top: 10px;
    margin-bottom: 5px;
}

/* Estilos para QRadioButton y QCheckBox */
QRadioButton::indicator, QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 2px solid #90b4e0;
    background-color: white;
}
QRadioButton::indicator {
    border-radius: 8px;
}
QCheckBox::indicator {
    border-radius: 3px;
}
QRadioButton::indicator:hover, QCheckBox::indicator:hover {
    border-color: var(--primary-color);
}
QRadioButton::indicator:checked, QCheckBox::indicator:checked {
    border-color: var(--primary-color);
    background-color: var(--primary-color);
}
QCheckBox::indicator:checked {
    image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOSIgdmlld0JveD0iMCAwIDEyIDkiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDQuNUw0LjUgOEwxMSAxIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgo8L3N2Zz4K);
}

/* Estilos para QTextEdit */
QTextEdit {
    background-color: white;
    border: 2px solid #90b4e0;
    border-radius: var(--radius-sm);
    padding: 8px;
    color: var(--text-primary);
}
QTextEdit:focus, QTextEdit:hover {
    border-color: var(--primary-color);
    border-width: 2px;
}

/* Estilos para el header y content area */
QWidget#header {
    background-color: var(--surface-color);
    border-bottom: 1px solid var(--border-color);
    padding: 10px;
}
QWidget#contentArea {
    background-color: var(--background-color);
    padding: 20px;
}

/* Estilos para estados y valores */
QLabel.status-pendiente {
    color: var(--warning-color);
    font-weight: 600;
}
QLabel.status-terminado {
    color: var(--success-color);
    font-weight: 600;
}
QLabel.money {
    color: var(--success-color);
    font-weight: 600;
}
QLabel.money-negative {
    color: var(--danger-color);
    font-weight: 600;
}

/* Tooltips y MessageBox */
QToolTip {
    background-color: var(--text-primary);
    color: white;
    border: none;
    border-radius: var(--radius-sm);
    padding: 8px;
    font-size: 8pt;
}
QMessageBox QPushButton {
    min-width: 80px;
}

/* Estilos específicos de secciones */
QGroupBox.measurements {
    border: 1px solid var(--border-color);
}
QGroupBox.models {
    border: 1px solid var(--primary-color);
}
QWidget#svg-option {
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    padding: 5px;
}
QWidget#svg-option:hover {
    border-color: var(--primary-color);
    background-color: var(--surface-color);
}
QGroupBox.billing {
    border: 1px solid var(--success-color);
}
QGroupBox.references {
    border: 1px solid var(--warning-color);
}
QWidget.total-section {
    background-color: var(--success-color);
    color: white;
    border-radius: var(--radius-md);
    padding: 15px;
}
QWidget.total-section QLabel {
    color: white;
    font-weight: 600;
}
QGroupBox.order-info {
    border: 1px solid var(--primary-color);
}
QGroupBox.financial-info {
    border: 1px solid var(--success-color);
}
QWidget#filterSection {
    background-color: var(--surface-color);
    border-radius: var(--radius-md);
    padding: 15px;
    margin-bottom: 15px;
}

QPushButton#abonoButton {
    background-color: #059669; /* Verde (éxito) */
    color: white;
}

QPushButton#abonoButton:hover {
    background-color: #047857; /* Verde más oscuro */
}
"""

# Interpolar los estilos
LIGHT_THEME_STYLES = interpolate_qss(STYLES_WITH_VARS)

# Eliminar las variables que ya no se usarán
DASHBOARD_STYLES = ""
CREATE_ORDER_STYLES = ""
VIEW_ORDER_STYLES = "" 