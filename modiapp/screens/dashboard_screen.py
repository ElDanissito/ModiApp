from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, 
                             QPushButton, QHBoxLayout, QHeaderView, QComboBox, 
                             QLineEdit, QDateEdit, QLabel, QMessageBox, QFileDialog)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate, Qt, Signal
from screens.create_order_screen import CreateOrderScreen
from screens.view_order_screen import ViewOrderScreen
from fpdf import FPDF
import os

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
        """Download order details as PDF"""
        order_data = self.db.get_order_details(order_id)
        if not order_data:
            QMessageBox.critical(self, "Error", "No se pudo obtener la información de la orden.")
            return

        # Diálogo para elegir la ruta de guardado
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", f"Orden_{order_data['order']['order_number']}.pdf", "PDF Files (*.pdf)")
        if not file_path:
            return

        try:
            pdf = FPDF(orientation='P', unit='mm', format='Letter')
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=10)
            pdf.set_font("Arial", size=10)

            # Logo
            logo_path = "modiapp/assets/Logo.png"
            if os.path.exists(logo_path):
                pdf.image(logo_path, x=10, y=10, w=40)
            pdf.set_xy(55, 10)
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "ORDEN DE TRABAJO", ln=1)
            pdf.set_font("Arial", size=10)
            pdf.ln(5)

            # Info principal
            order = order_data['order']
            pdf.cell(0, 8, f"N° Orden: {order['order_number']}", ln=1)
            pdf.cell(0, 8, f"Cliente: {order['client_name']}", ln=1)
            pdf.cell(0, 8, f"Fecha Orden: {order['order_date']}    Fecha Entrega: {order['delivery_date']}", ln=1)
            pdf.cell(0, 8, f"Estado: {order['status']}", ln=1)
            pdf.cell(0, 8, f"Valor Orden: $ {order['order_value']:,}    Abono: $ {order['deposit']:,}    Saldo: $ {order['order_value']-order['deposit']:,}", ln=1)
            pdf.ln(2)

            # Referencias
            if order_data['references']:
                pdf.set_font("Arial", 'B', 11)
                pdf.cell(0, 8, "Referencias:", ln=1)
                pdf.set_font("Arial", size=10)
                for ref in order_data['references']:
                    pdf.cell(0, 7, f"Ref: {ref['reference']}   Color: {ref['color']}   Valor: $ {ref['value']:,}", ln=1)
                pdf.ln(2)

            # Secciones de detalles
            def add_section(title, fields, data):
                pdf.set_font("Arial", 'B', 11)
                pdf.cell(0, 8, title, ln=1)
                pdf.set_font("Arial", size=10)
                for label, value in fields:
                    if value:
                        pdf.cell(0, 6, f"{label}: {value}", ln=1)
                pdf.ln(1)

            details = order_data['details']
            # Camisa
            if 'camisa' in details:
                camisa = details['camisa']
                fields = [
                    ("Cuello", camisa.get('Cuello')), ("Espalda", camisa.get('Espalda')), ("Hombro", camisa.get('Hombro')),
                    ("Manga x Cont.", camisa.get('Manga x Cont.')), ("Largo", camisa.get('Largo')), ("Cont. manga", camisa.get('Cont. manga')),
                    ("Pecho", camisa.get('Pecho')), ("Cintura", camisa.get('Cintura')), ("Cadera", camisa.get('Cadera')),
                    ("Prenda", camisa.get('Prenda')), ("Empaque", camisa.get('Empaque')),
                    ("Contextura Espalda", camisa.get('contextura_fisica_espalda')), ("Contextura Abdomen", camisa.get('contextura_fisica_abdomen')),
                    ("Vendedor", camisa.get('vendedor')),
                ]
                add_section("Medidas Camisa", fields, camisa)
                # Texto y Falda
                texto_fields = [
                    ("Iniciales", camisa.get('texto_iniciales')), ("Color", camisa.get('texto_color')),
                    ("Tipo", camisa.get('texto_tipo')), ("Bol", camisa.get('texto_bol')),
                    ("Fre", camisa.get('texto_fre')), ("Puñ", camisa.get('texto_puñ')),
                ]
                add_section("Texto Camisa", texto_fields, camisa)
                falda_fields = [
                    ("Color", camisa.get('falda_color')), ("Marip", camisa.get('falda_marip')), ("R. Abert", camisa.get('falda_r_abert')),
                ]
                add_section("Falda Camisa", falda_fields, camisa)
                # Modelos
                modelos_fields = [
                    ("Modelo Espalda", camisa.get('modelo_espalda')), ("Prespuente", camisa.get('modelo_espalda_prespuente')),
                    ("Pechera", 'Sí' if camisa.get('modelo_espalda_pechera')=='True' else ''),
                    ("Tapa Botón", 'Sí' if camisa.get('modelo_espalda_tapa_boton')=='True' else ''),
                    ("Modelo Bolsillo", camisa.get('modelo_bolsillo')),
                    ("Lado Bolsillo", camisa.get('lado_bolsillo')), ("Cantidad Bolsillo", camisa.get('cantidad_bolsillo')),
                    ("Modelo Puño", camisa.get('modelo_puno')), ("Textura Puño", camisa.get('textura_puno')),
                    ("Ancho Puño", camisa.get('ancho_cms_puno')), ("Modelo Cuello", camisa.get('modelo_cuello')),
                    ("Textura Cuello", camisa.get('textura_cuello')), ("Plum Cuello", camisa.get('plum_cuello')),
                    ("Bottom Down Cuello", camisa.get('bottom_down_cuello')),
                ]
                add_section("Modelos Camisa", modelos_fields, camisa)
                if camisa.get('observaciones'):
                    add_section("Observaciones Camisa", [("Observaciones", camisa.get('observaciones'))], camisa)

            # Saco
            if 'saco' in details:
                saco = details['saco']
                fields = [
                    ("Talle", saco.get('Talle')), ("Largo", saco.get('Largo')), ("1/2 espalda", saco.get('1/2 espalda')),
                    ("Hombro", saco.get('Hombro')), ("Manga", saco.get('Manga')), ("Pecho", saco.get('Pecho')),
                    ("Cintura", saco.get('Cintura')), ("Cadera", saco.get('Cadera')),
                    ("Estilo", saco.get('Estilo')), ("Cantidad Botón", saco.get('cantidad_boton')),
                    ("Solapa", saco.get('Solapa')), ("Ojal Solapa", 'Sí' if saco.get('ojal_solapa')=='True' else ''),
                    ("Bolsillo Inferior", saco.get('Bolsillo Inferior')),
                    ("Bolsillo Superior", saco.get('Bolsillo superior')),
                    ("Delantero", saco.get('Delantero')), ("Abertura", saco.get('Abertura')),
                    ("Modelo Chaleco", saco.get('Modelo chaleco')),
                    ("Diagonal Pecho", saco.get('chaleco_diagonal_pecho')),
                    ("Centro", saco.get('chaleco_centro')),
                    ("Largo Espalda", saco.get('chaleco_largo_espalda')),
                    ("Vendedor", saco.get('vendedor')),
                ]
                add_section("Medidas Saco", fields, saco)
                if saco.get('observaciones'):
                    add_section("Observaciones Saco", [("Observaciones", saco.get('observaciones'))], saco)
                if saco.get('observaciones_chaleco'):
                    add_section("Observaciones Chaleco", [("Observaciones", saco.get('observaciones_chaleco'))], saco)

            # Pantalón
            if 'pantalon' in details:
                pantalon = details['pantalon']
                fields = [
                    ("Cintura", pantalon.get('CINTURA')), ("Base", pantalon.get('BASE')), ("Largo", pantalon.get('LARGO')),
                    ("Pierna", pantalon.get('PIERNA')), ("Rodilla", pantalon.get('RODILLA')), ("Bota", pantalon.get('BOTA')),
                    ("Tiro", pantalon.get('TIRO')), ("Cont T", pantalon.get('CONT T')),
                    ("Bolsillo Delantero", pantalon.get('Bolsillo Delantero')),
                    ("Bolsillo Trasero", pantalon.get('Bolsillo Trasero')),
                    ("Terminado Bolsillo Trasero Botón", pantalon.get('terminado_bolsillo_trasero_boton')),
                    ("Terminado Bolsillo Trasero Oreja", pantalon.get('terminado_bolsillo_trasero_oreja')),
                    ("Terminado Bolsillo Trasero Parche", 'Sí' if pantalon.get('terminado_bolsillo_trasero_parche')=='True' else ''),
                    ("Terminado Bolsillo Trasero Parche Mod", pantalon.get('terminado_bolsillo_trasero_parche_mod')),
                    ("Pretina", pantalon.get('Pretina')),
                    ("Botón Pretina", 'Sí' if pantalon.get('Boton')=='True' else ''),
                    ("Gancho Pretina", 'Sí' if pantalon.get('Gancho')=='True' else ''),
                    ("Pasadores Pretina", pantalon.get('Pasadores')),
                    ("Forrado", pantalon.get('forrado')),
                    ("Forrado Opción 1", pantalon.get('forrado_opcion_1')),
                    ("Forrado Opción 2", pantalon.get('forrado_opcion_2')),
                    ("Especial", pantalon.get('Especial')),
                    ("Relojera", 'Sí' if pantalon.get('Relojera')=='True' else ''),
                    ("Bota", pantalon.get('Bota')),
                    ("Estilo Delantero", pantalon.get('estilo_delantero')),
                    ("Vendedor", pantalon.get('vendedor')),
                ]
                add_section("Medidas Pantalón", fields, pantalon)
                if pantalon.get('observaciones'):
                    add_section("Observaciones Pantalón", [("Observaciones", pantalon.get('observaciones'))], pantalon)

            pdf.output(file_path)
            QMessageBox.information(self, "Éxito", f"PDF guardado en: {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo exportar el PDF.\n{e}")

    def edit_order(self, order_id):
        """Edit an existing order"""
        # TODO: Implement order editing functionality
        QMessageBox.information(self, "Información", "Funcionalidad en desarrollo")

    def view_order(self, order_id):
        """View order details"""
        self.view_order_screen = ViewOrderScreen(self.db, order_id)
        self.view_order_screen.showMaximized() 