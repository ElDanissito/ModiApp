from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, 
                             QPushButton, QHBoxLayout, QHeaderView, QComboBox, 
                             QLineEdit, QDateEdit, QLabel, QMessageBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate, Qt, Signal
from screens.create_order_screen import CreateOrderScreen
from screens.view_order_screen import ViewOrderScreen

class DashboardScreen(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
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
        self.estado_combo.addItems(["Todos", "En proceso", "Terminado"])
        self.estado_combo.currentTextChanged.connect(self.apply_filters)
        header_layout.addWidget(self.estado_combo)

        # Date range filters
        date_filter_layout = QHBoxLayout()
        date_filter_layout.addWidget(QLabel("Desde:"))
        self.fecha_desde = QDateEdit(QDate.currentDate().addMonths(-1))
        self.fecha_desde.setCalendarPopup(True)
        self.fecha_desde.dateChanged.connect(self.apply_filters)
        date_filter_layout.addWidget(self.fecha_desde)

        date_filter_layout.addWidget(QLabel("Hasta:"))
        self.fecha_hasta = QDateEdit(QDate.currentDate())
        self.fecha_hasta.setCalendarPopup(True)
        self.fecha_hasta.dateChanged.connect(self.apply_filters)
        date_filter_layout.addWidget(self.fecha_hasta)
        
        header_layout.addLayout(date_filter_layout)
        
        self.buscar_input = QLineEdit()
        self.buscar_input.setPlaceholderText("Buscar por nombre del cliente")
        self.buscar_input.textChanged.connect(self.apply_filters)
        header_layout.addWidget(self.buscar_input)

        header_layout.addStretch()

        self.crear_button = QPushButton("Crear")
        self.crear_button.clicked.connect(self.show_create_order)
        header_layout.addWidget(self.crear_button)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels([
            "Estado", "Fecha Orden", "Fecha entrega", "N°", "Cliente", 
            "Valor Orden", "Abono", "Saldo", "Descargar", "Editar", "Ver"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Load initial data
        self.load_orders()

    def apply_filters(self):
        """Apply all filters to the orders list"""
        estado = self.estado_combo.currentText()
        fecha_desde = self.fecha_desde.date().toString("yyyy-MM-dd")
        fecha_hasta = self.fecha_hasta.date().toString("yyyy-MM-dd")
        search_text = self.buscar_input.text()

        # Get filtered orders from database
        orders = self.db.get_filtered_orders(
            estado=estado if estado != "Todos" else None,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
            search_text=search_text
        )
        
        self.update_table(orders)

    def load_orders(self):
        """Load orders from database"""
        self.apply_filters()

    def update_table(self, orders):
        """Update the table with the given orders"""
        self.table.setRowCount(len(orders))
        
        for row, order in enumerate(orders):
            # Status
            self.table.setItem(row, 0, QTableWidgetItem(order['status']))
            
            # Dates
            self.table.setItem(row, 1, QTableWidgetItem(order['order_date']))
            self.table.setItem(row, 2, QTableWidgetItem(order['delivery_date']))
            
            # Order number and client
            self.table.setItem(row, 3, QTableWidgetItem(order['order_number']))
            self.table.setItem(row, 4, QTableWidgetItem(order['client_name']))
            
            # Financial info
            self.table.setItem(row, 5, QTableWidgetItem(f"$ {order['order_value']:,}"))
            self.table.setItem(row, 6, QTableWidgetItem(f"$ {order['deposit']:,}"))
            saldo = order['order_value'] - order['deposit']
            self.table.setItem(row, 7, QTableWidgetItem(f"$ {saldo:,}"))
            
            # Action buttons
            download_btn = QPushButton("Descargar")
            download_btn.clicked.connect(lambda checked, oid=order['id']: self.download_order(oid))
            self.table.setCellWidget(row, 8, download_btn)
            
            edit_btn = QPushButton("Editar")
            edit_btn.clicked.connect(lambda checked, oid=order['id']: self.edit_order(oid))
            self.table.setCellWidget(row, 9, edit_btn)
            
            view_btn = QPushButton("Ver")
            view_btn.clicked.connect(lambda checked, oid=order['id']: self.view_order(oid))
            self.table.setCellWidget(row, 10, view_btn)

    def show_create_order(self):
        """Show the create order screen"""
        self.create_order_screen = CreateOrderScreen(self.db)
        self.create_order_screen.showMaximized()
        self.create_order_screen.order_created.connect(self.load_orders)

    def download_order(self, order_id):
        """Download order details"""
        # TODO: Implement order download functionality
        QMessageBox.information(self, "Información", "Funcionalidad en desarrollo")

    def edit_order(self, order_id):
        """Edit an existing order"""
        # TODO: Implement order editing functionality
        QMessageBox.information(self, "Información", "Funcionalidad en desarrollo")

    def view_order(self, order_id):
        """View order details"""
        self.view_order_screen = ViewOrderScreen(self.db, order_id)
        self.view_order_screen.showMaximized() 