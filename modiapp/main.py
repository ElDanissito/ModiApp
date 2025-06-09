import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from modiapp.screens.dashboard_screen import DashboardScreen
# We will create this file in the next step
from modiapp.screens.create_order_screen import CreateOrderScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ferdinand")
        self.resize(1200, 800)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.dashboard_screen = DashboardScreen()
        self.dashboard_screen.crear_button.clicked.connect(self.show_create_order_screen)
        
        self.create_order_screen = CreateOrderScreen()
        self.create_order_screen.back_button.clicked.connect(self.show_dashboard_screen)

        self.stacked_widget.addWidget(self.dashboard_screen)
        self.stacked_widget.addWidget(self.create_order_screen)

    def show_create_order_screen(self):
        self.stacked_widget.setCurrentWidget(self.create_order_screen)

    def show_dashboard_screen(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 