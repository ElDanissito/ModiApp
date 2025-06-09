from PySide6.QtWidgets import (QWidget, QVBoxLayout, QScrollArea, QPushButton, 
                             QHBoxLayout, QLabel, QGroupBox, QGridLayout,
                             QLineEdit, QDateEdit, QRadioButton, QTextEdit, QFrame)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QDate

class CreateOrderScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header with Back Button
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        
        logo_label = QLabel()
        pixmap = QPixmap("modiapp/assets/Logo.png")
        logo_label.setPixmap(pixmap.scaledToWidth(250))
        header_layout.addWidget(logo_label)
        header_layout.addStretch()

        self.back_button = QPushButton("← Atras")
        header_layout.addWidget(self.back_button)
        main_layout.addWidget(header_widget)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # Main content widget
        self.content_widget = QWidget()
        scroll_area.setWidget(self.content_widget)

        # Layout for the content widget
        content_layout = QVBoxLayout(self.content_widget)
        
        # Client and Date Header
        header_group = QGroupBox()
        header_layout = QGridLayout(header_group)
        
        header_layout.addWidget(QLabel("<b>Cliente:</b>"), 0, 0)
        header_layout.addWidget(QLineEdit(), 0, 1)

        header_layout.addWidget(QLabel("Fecha Orden"), 0, 2)
        fecha_orden_edit = QDateEdit(QDate.currentDate())
        fecha_orden_edit.setCalendarPopup(True)
        header_layout.addWidget(fecha_orden_edit, 0, 3)
        
        header_layout.addWidget(QLabel("Fecha Entrega"), 0, 4)
        fecha_entrega_edit = QDateEdit(QDate.currentDate())
        fecha_entrega_edit.setCalendarPopup(True)
        header_layout.addWidget(fecha_entrega_edit, 0, 5)

        header_layout.addWidget(QLabel("<b>Ferdinand N° 0000</b>"), 0, 6, Qt.AlignRight)

        content_layout.addWidget(header_group)

        # Main sections layout
        main_sections_layout = QHBoxLayout()
        content_layout.addLayout(main_sections_layout)

        # Left column
        left_column_layout = QVBoxLayout()
        main_sections_layout.addLayout(left_column_layout)

        camisa_group = QGroupBox("MEDIDAS CAMISA")
        camisa_layout = QVBoxLayout(camisa_group)
        left_column_layout.addWidget(camisa_group)

        # Medidas
        medidas_camisa_layout = QGridLayout()
        camisa_layout.addLayout(medidas_camisa_layout)

        fields = ["Cuello", "Espalda", "Hombro", "Manga x Cont.", "Largo", "Cont. manga", "Pecho", "Cintura", "Cadera"]
        for i, field in enumerate(fields):
            medidas_camisa_layout.addWidget(QLabel(field), 0, i)
            medidas_camisa_layout.addWidget(QLineEdit(), 1, i)

        # Modelos
        modelos_layout = QHBoxLayout()
        camisa_layout.addLayout(modelos_layout)

        # Modelo Espalda
        espalda_group = QGroupBox("Modelo Espalda")
        espalda_layout = QGridLayout(espalda_group)
        for i in range(6):
            espalda_layout.addWidget(QPushButton(f"Img {i+1}"), i // 3, i % 3)
        modelos_layout.addWidget(espalda_group)

        # Modelo Bolsillo
        bolsillo_group = QGroupBox("Modelo Bolsillo")
        bolsillo_layout = QGridLayout(bolsillo_group)
        for i in range(13):
            bolsillo_layout.addWidget(QPushButton(f"Img {i+1}"), i // 4, i % 4)
        modelos_layout.addWidget(bolsillo_group)

        # --- Puño y Cuello ---
        puño_cuello_layout = QHBoxLayout()
        camisa_layout.addLayout(puño_cuello_layout)

        # --- Modelo Puño ---
        puño_group = QGroupBox("Modelo Puño")
        puño_cuello_layout.addWidget(puño_group)
        puño_main_layout = QHBoxLayout(puño_group)
        
        textura_puño_layout = QVBoxLayout()
        textura_puño_layout.addWidget(QLabel("TEXTURA"))
        textura_puño_layout.addWidget(QRadioButton("Rígido"))
        textura_puño_layout.addWidget(QRadioButton("Normal"))
        textura_puño_layout.addWidget(QRadioButton("Suave"))
        textura_puño_layout.addStretch()
        puño_main_layout.addLayout(textura_puño_layout)

        line_puño = QFrame()
        line_puño.setFrameShape(QFrame.VLine)
        line_puño.setFrameShadow(QFrame.Sunken)
        puño_main_layout.addWidget(line_puño)

        puño_grid_layout = QGridLayout()
        puño_main_layout.addLayout(puño_grid_layout)

        puño_grid_layout.addWidget(QRadioButton("R.D"), 0, 0)
        puño_grid_layout.addWidget(QRadioButton("R.A"), 0, 1)
        puño_grid_layout.addWidget(QRadioButton("PUNTA"), 0, 2)

        puño_grid_layout.addWidget(QRadioButton("D.USO"), 1, 0)
        puño_grid_layout.addWidget(QRadioButton("R.A.2B"), 1, 1)
        puño_grid_layout.addWidget(QRadioButton("MAN"), 1, 2)

        puño_grid_layout.addWidget(QRadioButton("DISEÑO"), 2, 0)
        puño_grid_layout.addWidget(QLineEdit("ANCHO CMS."), 2, 1)
        puño_grid_layout.addWidget(QRadioButton("MANGA CORTA"), 2, 2)

        # --- Modelo Cuello ---
        cuello_group = QGroupBox("Modelo Cuello")
        puño_cuello_layout.addWidget(cuello_group)
        cuello_main_layout = QHBoxLayout(cuello_group)

        textura_cuello_layout = QVBoxLayout()
        textura_cuello_layout.addWidget(QLabel("TEXTURA"))
        textura_cuello_layout.addWidget(QRadioButton("Rígido"))
        textura_cuello_layout.addWidget(QRadioButton("Normal"))
        textura_cuello_layout.addWidget(QRadioButton("Suave"))
        textura_cuello_layout.addStretch()
        cuello_main_layout.addLayout(textura_cuello_layout)

        line_cuello = QFrame()
        line_cuello.setFrameShape(QFrame.VLine)
        line_cuello.setFrameShadow(QFrame.Sunken)
        cuello_main_layout.addWidget(line_cuello)

        cuello_grid_layout = QGridLayout()
        cuello_main_layout.addLayout(cuello_grid_layout)

        cuello_options = [
            "Pegasso", "Valentino C", "Crown", "Givenchy", "Pajarito",
            "", "Valentino L", "", "Neru", "Royal",
            "OTRO - CUAL?", "Bottom Down", "Plum. Fija.", "Plum. Rever.",
            "", "", "Ext", "Int", ""
        ]
        for i, option in enumerate(cuello_options):
            if "OTRO" in option or "ANCHO" in option:
                cuello_grid_layout.addWidget(QLineEdit(option), i // 5, i % 5)
            elif option:
                cuello_grid_layout.addWidget(QRadioButton(option), i // 5, i % 5)

        # --- Otros Detalles ---
        detalles_layout = QGridLayout()
        camisa_layout.addLayout(detalles_layout)

        iniciales_group = QGroupBox("TEXTO")
        iniciales_layout = QGridLayout(iniciales_group)
        iniciales_fields = ["Color", "Tipo", "Bol", "Fre.", "Puñ"]
        for i, field in enumerate(iniciales_fields):
            iniciales_layout.addWidget(QLabel(field), 0, i)
            iniciales_layout.addWidget(QLineEdit(), 1, i)
        detalles_layout.addWidget(iniciales_group, 0, 0)

        falda_group = QGroupBox("Falda")
        falda_layout = QGridLayout(falda_group)
        falda_fields = ["Color", "Marip", "R. Abert"]
        for i, field in enumerate(falda_fields):
            falda_layout.addWidget(QLabel(field), 0, i)
            falda_layout.addWidget(QLineEdit(), 1, i)
        detalles_layout.addWidget(falda_group, 1, 0)
        
        prenda_empaque_layout = QVBoxLayout()
        detalles_layout.addLayout(prenda_empaque_layout, 0, 1, 2, 1)

        prenda_group = QGroupBox("Prenda")
        prenda_layout = QHBoxLayout(prenda_group)
        prenda_layout.addWidget(QRadioButton("Camisa"))
        prenda_layout.addWidget(QRadioButton("Guayabera"))
        prenda_empaque_layout.addWidget(prenda_group)

        empaque_group = QGroupBox("Empaque")
        empaque_layout = QHBoxLayout(empaque_group)
        empaque_layout.addWidget(QRadioButton("Gancho"))
        empaque_layout.addWidget(QRadioButton("Doblada"))
        prenda_empaque_layout.addWidget(empaque_group)
        
        contextura_group = QGroupBox("Contextura Fisica")
        contextura_layout = QGridLayout(contextura_group)
        contextura_layout.addWidget(QLabel("Espalda"), 0, 0)
        contextura_layout.addWidget(QLineEdit(), 1, 0)
        contextura_layout.addWidget(QLabel("Abdomen"), 0, 1)
        contextura_layout.addWidget(QLineEdit(), 1, 1)
        detalles_layout.addWidget(contextura_group, 0, 2, 2, 1)

        observaciones_group = QGroupBox("Observaciones")
        obs_layout = QVBoxLayout(observaciones_group)
        obs_layout.addWidget(QTextEdit())
        
        vendedor_layout = QVBoxLayout()
        vendedor_layout.addWidget(QLabel("Vendedor:"))
        vendedor_layout.addWidget(QLineEdit())

        obs_vend_layout = QHBoxLayout()
        obs_vend_layout.addWidget(observaciones_group, 3)
        obs_vend_layout.addLayout(vendedor_layout, 1)
        camisa_layout.addLayout(obs_vend_layout)

        # Right column
        right_column_layout = QVBoxLayout()
        main_sections_layout.addLayout(right_column_layout)

        saco_group = QGroupBox("MEDIDAS SACO")
        saco_layout = QVBoxLayout(saco_group)
        right_column_layout.addWidget(saco_group)

        # Medidas
        medidas_saco_layout = QGridLayout()
        saco_layout.addLayout(medidas_saco_layout)
        
        fields = ["Talle", "Largo", "1/2 Espalda", "Hombro", "Manga", "Pecho", "Cintura", "Cadera"]
        for i, field in enumerate(fields):
            medidas_saco_layout.addWidget(QLabel(field), 0, i)
            medidas_saco_layout.addWidget(QLineEdit(), 1, i)

        # Pantalon section
        pantalon_group = QGroupBox("MEDIDAS PANTALON")
        content_layout.addWidget(pantalon_group)

        # Medidas
        pantalon_layout = QVBoxLayout(pantalon_group)
        medidas_pantalon_layout = QGridLayout()
        pantalon_layout.addLayout(medidas_pantalon_layout)

        fields = ["Cintura", "Base", "Largo", "Pierna", "Rodilla", "Bota", "Tiro", "CONT. T"]
        for i, field in enumerate(fields):
            medidas_pantalon_layout.addWidget(QLabel(field), 0, i)
            medidas_pantalon_layout.addWidget(QLineEdit(), 1, i)

        # Billing section
        billing_group = QGroupBox("FACTURACIÓN")
        content_layout.addWidget(billing_group)

        # Add more widgets here 