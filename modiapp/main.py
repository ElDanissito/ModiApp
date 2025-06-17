import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
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
        self.setWindowIcon(QIcon(resource_path("modiapp/assets/Logo.png")))
        
        # Create and show dashboard
        self.dashboard = DashboardScreen(self.db)
        self.dashboard.showMaximized()

def main():
    app = MainWindow(sys.argv)
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 