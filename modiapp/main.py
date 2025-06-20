import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

# Add the current directory to Python path for PyInstaller
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import modules
from screens.dashboard_screen import DashboardScreen
from database import Database

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MainWindow(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        
        # Initialize database
        self.db = Database()
        
        # Set application icon
        self.setWindowIcon(QIcon(resource_path("modiapp/assets/favicon.ico")))
        
        # Aplicar estilos globales
        self.apply_global_styles()
        
        # Create and show dashboard
        self.dashboard = DashboardScreen(self.db)
        self.dashboard.showMaximized()

    def apply_global_styles(self):
        """Aplicar estilos globales a toda la aplicación"""
        from styles import LIGHT_THEME_STYLES
        
        # Aplicar estilos base a toda la aplicación
        self.setStyleSheet(LIGHT_THEME_STYLES)
        
        # Configurar la aplicación para usar el modo claro por defecto
        self.setStyle("Fusion")  # Usar el estilo Fusion que es más moderno

def main():
    app = MainWindow(sys.argv)
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 