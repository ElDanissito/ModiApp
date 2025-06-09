from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, 
                             QPushButton, QHBoxLayout, QHeaderView, QComboBox, 
                             QLineEdit, QDateEdit, QLabel)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate

class DashboardScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Header with Logo
        header_logo_layout = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap("modiapp/assets/Logo.png")
        logo_label.setPixmap(pixmap.scaledToWidth(250))
        header_logo_layout.addWidget(logo_label)
        header_logo_layout.addStretch()
        self.layout.addLayout(header_logo_layout)

        # Header
        header_layout = QHBoxLayout()
        self.layout.addLayout(header_layout)

        # Controls
        self.estado_combo = QComboBox()
        self.estado_combo.addItems(["Estado", "En proceso", "Terminado"])
        header_layout.addWidget(self.estado_combo)

        self.fecha_edit = QDateEdit(QDate.currentDate())
        self.fecha_edit.setCalendarPopup(True)
        header_layout.addWidget(self.fecha_edit)
        
        self.buscar_input = QLineEdit()
        self.buscar_input.setPlaceholderText("Buscar")
        header_layout.addWidget(self.buscar_input)

        header_layout.addStretch()

        self.crear_button = QPushButton("Crear")
        header_layout.addWidget(self.crear_button)


        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels([
            "Estado", "Fecha Orden", "Fecha entrega", "N°", "Cliente", 
            "Valor Orden", "Abono", "Saldo", "Descargar", "Editar", "Ver"
        ])
        self.layout.addWidget(self.table)

        self.load_orders()

    def load_orders(self):
        # Sample data
        orders = [
            ("En proceso", "21-03-2022", "23-03-2022", "1596", "Juan Perez", "$ 200,000.00", "$ 150,000.00", "$ 50,000.00"),
            ("En proceso", "21-03-2022", "22-03-2022", "1595", "Sofia Gutierrez", "$ 200,000.00", "$ 150,000.00", "$ 50,000.00"),
            ("Terminado", "21-03-2022", "09-03-2022", "1593", "Sofia Gutierrez", "$ 200,000.00", "$ 150,000.00", "$ 50,000.00"),
            ("Terminado", "21-03-2022", "09-03-2022", "1593", "Sofia Gutierrez", "$ 200,000.00", "$ 150,000.00", "$ 50,000.00"),
            ("Terminado", "21-03-2022", "09-03-2022", "1593", "Sofia Gutierrez", "$ 200,000.00", "$ 150,000.00", "$ 50,000.00"),
            ("Terminado", "21-03-2022", "10-03-2022", "1592", "Sofia Gutierrez", "$ 200,000.00", "$ 150,000.00", "$ 50,000.00"),
        ]

        self.table.setRowCount(len(orders))

        for row, order in enumerate(orders):
            for col, data in enumerate(order):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))
            
            self.table.setCellWidget(row, 8, QPushButton("Descargar"))
            self.table.setCellWidget(row, 9, QPushButton("Editar"))
            self.table.setCellWidget(row, 10, QPushButton("Ver"))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 