from PySide6.QtWidgets import (QWidget, QVBoxLayout, QScrollArea, QPushButton, 
                             QHBoxLayout, QLabel, QGroupBox, QGridLayout,
                             QLineEdit, QDateEdit, QRadioButton, QTextEdit, QFrame,
                             QComboBox, QCheckBox, QButtonGroup)
from PySide6.QtSvgWidgets import QSvgWidget
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
        espalda_main_layout = QVBoxLayout(espalda_group)

        espalda_grid_layout = QGridLayout()
        
        # Crear un grupo de botones de radio para que solo uno pueda ser seleccionado
        self.espalda_button_group = QButtonGroup()

        espalda_options = [
            ("Tableta_1.svg", "Tableta"),
            ("Prenses_2.svg", "Prenses"),
            ("Fuelle_3.svg", "Fuelle"),
            ("Doble Tableta_4.svg", "Doble Tableta"),
            ("Pinzas_5.svg", "Pinzas"),
            ("Lisa_6.svg", "Lisa")
        ]

        for i, (img_file, name) in enumerate(espalda_options):
            # Contenedor para la imagen y el radio button
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 0)
            option_layout.setSpacing(5)
            
            # Widget para la imagen SVG
            image_widget = QSvgWidget(f"docs/svgs/Modelo Espalda/{img_file}")
            image_widget.setFixedSize(80, 80)
            
            radio_button = QRadioButton(name)
            self.espalda_button_group.addButton(radio_button)

            option_layout.addWidget(image_widget)
            option_layout.addWidget(radio_button, alignment=Qt.AlignCenter)
            
            espalda_grid_layout.addWidget(option_container, i // 3, i % 3)

        espalda_main_layout.addLayout(espalda_grid_layout)

        # Opciones adicionales
        additional_options_layout = QHBoxLayout()

        # Prespuente
        prespuente_layout = QHBoxLayout()
        prespuente_layout.addWidget(QLabel("Prespuente:"))
        prespuente_combo = QComboBox()
        prespuente_combo.addItems(["1/16", "1/8", "3/16", "1/4", "Dob"])
        prespuente_layout.addWidget(prespuente_combo)
        additional_options_layout.addLayout(prespuente_layout)

        # Pechera
        pechera_checkbox = QCheckBox("Pechera")
        additional_options_layout.addWidget(pechera_checkbox)

        # Tapa botón
        tapa_boton_checkbox = QCheckBox("Tapa botón")
        additional_options_layout.addWidget(tapa_boton_checkbox)
        
        espalda_main_layout.addLayout(additional_options_layout)
        modelos_layout.addWidget(espalda_group)

        # Modelo Bolsillo
        bolsillo_group = QGroupBox("Modelo Bolsillo")
        bolsillo_main_layout = QVBoxLayout(bolsillo_group)
        modelos_layout.addWidget(bolsillo_group)

        self.modelo_bolsillo_button_group = QButtonGroup()
        bolsillo_grid_layout = QGridLayout()
        
        for i in range(13):
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0,0,0,0)
            
            svg_widget = QSvgWidget(f"docs/svgs/Modelo Bolsillo/{i+1}.svg")
            svg_widget.setFixedSize(60, 60)
            
            rb = QRadioButton(f"Modelo {i+1}")
            self.modelo_bolsillo_button_group.addButton(rb)
            
            option_layout.addWidget(svg_widget)
            option_layout.addWidget(rb, alignment=Qt.AlignCenter)
            bolsillo_grid_layout.addWidget(option_container, i // 5, i % 5)

        bolsillo_main_layout.addLayout(bolsillo_grid_layout)

        # Opciones adicionales de bolsillo
        additional_bolsillo_layout = QHBoxLayout()
        
        # Lado y Posición
        lado_pos_group = QGroupBox("Lado y Posición")
        lado_pos_layout = QHBoxLayout(lado_pos_group)
        self.lado_bolsillo_group = QButtonGroup()
        for text in ["Izq", "Der"]:
            rb = QRadioButton(text)
            self.lado_bolsillo_group.addButton(rb)
            lado_pos_layout.addWidget(rb)
        additional_bolsillo_layout.addWidget(lado_pos_group)

        # Cantidad
        cant_layout = QHBoxLayout()
        cant_layout.addWidget(QLabel("Cant.:"))
        self.cantidad_bolsillo_edit = QLineEdit()
        self.cantidad_bolsillo_edit.setFixedWidth(40)
        cant_layout.addWidget(self.cantidad_bolsillo_edit)
        additional_bolsillo_layout.addLayout(cant_layout)
        
        # Opción NO
        rb_no_bolsillo = QRadioButton("NO")
        self.modelo_bolsillo_button_group.addButton(rb_no_bolsillo)
        additional_bolsillo_layout.addWidget(rb_no_bolsillo)
        
        bolsillo_main_layout.addLayout(additional_bolsillo_layout)
        
        # Lógica para habilitar/deshabilitar
        self.bolsillo_widgets_to_toggle = [lado_pos_group, self.cantidad_bolsillo_edit]

        def toggle_bolsillo_options(button, checked):
            # Deshabilitar si 'NO' está seleccionado
            is_no_button = (button.text() == "NO")
            if is_no_button and checked:
                for widget in self.bolsillo_widgets_to_toggle:
                    widget.setEnabled(False)
                # Deseleccionar cualquier modelo de bolsillo si se selecciona NO
                if self.modelo_bolsillo_button_group.checkedButton() and self.modelo_bolsillo_button_group.checkedButton().text() != "NO":
                     self.modelo_bolsillo_button_group.setExclusive(False)
                     self.modelo_bolsillo_button_group.checkedButton().setChecked(False)
                     self.modelo_bolsillo_button_group.setExclusive(True)

            # Habilitar si un modelo está seleccionado
            elif not is_no_button and checked:
                for widget in self.bolsillo_widgets_to_toggle:
                    widget.setEnabled(True)

        self.modelo_bolsillo_button_group.buttonToggled.connect(toggle_bolsillo_options)

        # Estado inicial
        rb_no_bolsillo.setChecked(True)

        # --- Puño y Cuello ---
        puño_cuello_layout = QHBoxLayout()
        camisa_layout.addLayout(puño_cuello_layout)

        # --- Modelo Puño ---
        puño_group = QGroupBox("Modelo Puño")
        puño_cuello_layout.addWidget(puño_group)
        puño_main_layout = QHBoxLayout(puño_group)
        
        self.textura_puno_button_group = QButtonGroup()
        textura_puño_layout = QVBoxLayout()
        textura_puño_layout.addWidget(QLabel("TEXTURA"))

        rb_rigido = QRadioButton("Rígido")
        self.textura_puno_button_group.addButton(rb_rigido)
        textura_puño_layout.addWidget(rb_rigido)

        rb_normal = QRadioButton("Normal")
        self.textura_puno_button_group.addButton(rb_normal)
        textura_puño_layout.addWidget(rb_normal)

        rb_suave = QRadioButton("Suave")
        self.textura_puno_button_group.addButton(rb_suave)
        textura_puño_layout.addWidget(rb_suave)

        textura_puño_layout.addStretch()
        puño_main_layout.addLayout(textura_puño_layout)

        line_puño = QFrame()
        line_puño.setFrameShape(QFrame.VLine)
        line_puño.setFrameShadow(QFrame.Sunken)
        puño_main_layout.addWidget(line_puño)

        self.modelo_puno_button_group = QButtonGroup()
        puño_grid_layout = QGridLayout()
        puño_main_layout.addLayout(puño_grid_layout)

        puno_options = [
            ("RD.svg", "R.D", 0, 0), ("RA.svg", "R.A", 0, 1), ("PUNTA.svg", "PUNTA", 0, 2),
            ("D USO.svg", "D.USO", 1, 0), ("RA2B.svg", "R.A.2B", 1, 1), ("MAN.svg", "MAN", 1, 2),
            (None, "DISEÑO", 2, 0), (None, "MANGA CORTA", 2, 2)
        ]

        for img_file, text, row, col in puno_options:
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 0)
            option_layout.setSpacing(5)

            if img_file:
                image_widget = QSvgWidget(f"docs/svgs/Modelo Puño/{img_file}")
                image_widget.setFixedSize(80, 80)
            else:
                image_widget = QLabel(text)
                image_widget.setFixedSize(80, 80)
                image_widget.setStyleSheet("border: 1px solid black;")
                image_widget.setAlignment(Qt.AlignCenter)

            radio_button = QRadioButton(text)
            self.modelo_puno_button_group.addButton(radio_button)

            option_layout.addWidget(image_widget)
            option_layout.addWidget(radio_button, alignment=Qt.AlignCenter)

            puño_grid_layout.addWidget(option_container, row, col)

        puño_grid_layout.addWidget(QLineEdit("ANCHO CMS."), 2, 1)

        # --- Modelo Cuello ---
        cuello_group = QGroupBox("Modelo Cuello")
        puño_cuello_layout.addWidget(cuello_group)
        cuello_main_layout = QHBoxLayout(cuello_group)

        # --- Textura Section ---
        self.textura_cuello_button_group = QButtonGroup()
        textura_cuello_layout = QVBoxLayout()
        textura_cuello_layout.addWidget(QLabel("TEXTURA"))
        for text in ["Rígido", "Normal", "Suave"]:
            rb = QRadioButton(text)
            self.textura_cuello_button_group.addButton(rb)
            textura_cuello_layout.addWidget(rb)
        textura_cuello_layout.addStretch()
        cuello_main_layout.addLayout(textura_cuello_layout)

        line_cuello = QFrame()
        line_cuello.setFrameShape(QFrame.VLine)
        line_cuello.setFrameShadow(QFrame.Sunken)
        cuello_main_layout.addWidget(line_cuello)

        # --- Modelos Section ---
        self.modelo_cuello_button_group = QButtonGroup()
        modelos_cuello_layout = QVBoxLayout()
        cuello_main_layout.addLayout(modelos_cuello_layout)

        cuello_grid_layout = QGridLayout()
        modelos_cuello_layout.addLayout(cuello_grid_layout)

        simple_cuello_options = [
            "Pegasso", "Valentino C", "Crown", "Givenchy", "Pajarito",
            "Valentino L", "Neru", "Royal", "Plum. Fija.", "Plum. Rever."
        ]
        for i, option_text in enumerate(simple_cuello_options):
            rb = QRadioButton(option_text)
            self.modelo_cuello_button_group.addButton(rb)
            cuello_grid_layout.addWidget(rb, i % 5, i // 5)

        # --- Bottom Down Section ---
        bottom_down_widget = QWidget()
        bottom_down_layout = QHBoxLayout(bottom_down_widget)
        bottom_down_layout.setContentsMargins(0,0,0,0)
        rb_bottom_down = QRadioButton("Bottom Down")
        self.modelo_cuello_button_group.addButton(rb_bottom_down)
        bottom_down_layout.addWidget(rb_bottom_down)

        self.bottom_down_sub_group = QButtonGroup()
        rb_ext = QRadioButton("Ext")
        rb_int = QRadioButton("Int")
        self.bottom_down_sub_group.addButton(rb_ext)
        self.bottom_down_sub_group.addButton(rb_int)
        rb_ext.setEnabled(False)
        rb_int.setEnabled(False)

        def toggle_bottom_down(checked):
            rb_ext.setEnabled(checked)
            rb_int.setEnabled(checked)
            if checked:
                rb_ext.setChecked(True)
        rb_bottom_down.toggled.connect(toggle_bottom_down)

        bottom_down_layout.addWidget(rb_ext)
        bottom_down_layout.addWidget(rb_int)
        modelos_cuello_layout.addWidget(bottom_down_widget)

        # --- Otro Section ---
        otro_widget = QWidget()
        otro_layout = QHBoxLayout(otro_widget)
        otro_layout.setContentsMargins(0,0,0,0)
        rb_otro = QRadioButton("OTRO - CUAL?")
        self.modelo_cuello_button_group.addButton(rb_otro)
        otro_layout.addWidget(rb_otro)

        otro_line_edit = QLineEdit()
        otro_line_edit.setPlaceholderText("Especificar otro modelo")
        otro_line_edit.setEnabled(False)
        rb_otro.toggled.connect(otro_line_edit.setEnabled)
        otro_layout.addWidget(otro_line_edit)
        modelos_cuello_layout.addWidget(otro_widget)

        modelos_cuello_layout.addStretch()

        # --- Otros Detalles ---
        detalles_layout = QGridLayout()
        camisa_layout.addLayout(detalles_layout)

        iniciales_group = QGroupBox("TEXTO")
        iniciales_layout = QGridLayout(iniciales_group)
        iniciales_fields = ["Iniciales", "Color", "Tipo", "Bol", "Fre.", "Puñ"]
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