from PySide6.QtWidgets import (QWidget, QVBoxLayout, QScrollArea, QPushButton, 
                             QHBoxLayout, QLabel, QGroupBox, QGridLayout,
                             QLineEdit, QDateEdit, QRadioButton, QTextEdit, QFrame,
                             QComboBox, QCheckBox, QButtonGroup, QTableWidget, QHeaderView, QTableWidgetItem)
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QPixmap, QValidator
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
        self.cliente_name_edit = QLineEdit()
        header_layout.addWidget(self.cliente_name_edit, 0, 1)

        # Define date widgets before adding them to layout
        self.fecha_orden_edit = QDateEdit(QDate.currentDate())
        self.fecha_orden_edit.setCalendarPopup(True)
        self.fecha_entrega_edit = QDateEdit(QDate.currentDate())
        self.fecha_entrega_edit.setCalendarPopup(True)

        # Add widgets to layout with new spacing
        header_layout.addWidget(QLabel("Fecha Orden"), 0, 2)
        header_layout.addWidget(self.fecha_orden_edit, 0, 3)
        
        header_layout.addWidget(QLabel("Fecha Entrega"), 0, 5)
        header_layout.addWidget(self.fecha_entrega_edit, 0, 6)

        header_layout.addWidget(QLabel("<b>Ferdinand N° 0000</b>"), 0, 8, Qt.AlignRight)

        # Set stretch factors to distribute space
        header_layout.setColumnStretch(1, 4)  # Client field
        header_layout.setColumnStretch(4, 1)  # Spacer between dates
        header_layout.setColumnStretch(7, 1)  # Spacer before order number

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

            option_layout.addWidget(image_widget, alignment=Qt.AlignCenter)
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
        
        bolsillo_names = [
            "Fuelle #11", "En punta con\nTapa #5", "En Punta\nImitación Tapa #8",
            "En Punta Liso #1", "En Punta con\nDobles #4", "Diagonal Liso #2",
            "Diagonal Tableta #2", "Diagonal con\nTapa #13", "Redondo Liso #7",
            "Redondo con\nTapa #5", "Redondo Corte\nDespuntado #9", "Redondo Oreja\ncon Botón #10",
            "Cuadrado #3"
        ]

        for i in range(13):
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0,0,0,0)
            
            svg_widget = QSvgWidget(f"docs/svgs/Modelo Bolsillo/{i+1}.svg")
            svg_widget.setFixedSize(60, 60)
            
            rb = QRadioButton(bolsillo_names[i])
            self.modelo_bolsillo_button_group.addButton(rb)
            
            option_layout.addWidget(svg_widget, alignment=Qt.AlignCenter)
            option_layout.addWidget(rb, alignment=Qt.AlignCenter)
            bolsillo_grid_layout.addWidget(option_container, i // 5, i % 5)

        bolsillo_main_layout.addLayout(bolsillo_grid_layout)

        # Opciones adicionales de bolsillo
        additional_bolsillo_layout = QHBoxLayout()
        
        # Container for left-side options
        left_options_container = QWidget()
        left_options_layout = QHBoxLayout(left_options_container)
        left_options_layout.setContentsMargins(0,0,0,0)
        left_options_layout.setSpacing(5)

        # Lado y Posición
        lado_pos_group = QGroupBox("Lado y Posición")
        lado_pos_layout = QHBoxLayout(lado_pos_group)
        self.lado_bolsillo_group = QButtonGroup()
        for text in ["Izq", "Der"]:
            rb = QRadioButton(text)
            self.lado_bolsillo_group.addButton(rb)
            lado_pos_layout.addWidget(rb)
        left_options_layout.addWidget(lado_pos_group)

        # Cantidad
        left_options_layout.addWidget(QLabel("Cant.:"))
        self.cantidad_bolsillo_edit = QLineEdit()
        self.cantidad_bolsillo_edit.setFixedWidth(70)
        left_options_layout.addWidget(self.cantidad_bolsillo_edit)
        
        additional_bolsillo_layout.addWidget(left_options_container)
        additional_bolsillo_layout.addStretch()

        # Opción NO
        rb_no_bolsillo = QRadioButton("NO")
        self.modelo_bolsillo_button_group.addButton(rb_no_bolsillo)
        additional_bolsillo_layout.addWidget(rb_no_bolsillo)
        
        bolsillo_main_layout.addLayout(additional_bolsillo_layout)
        
        # Lógica para habilitar/deshabilitar
        self.bolsillo_widgets_to_toggle = [left_options_container]

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
            (None, "DISEÑO", 2, 0), (None, "MANGA\nCORTA", 2, 2)
        ]

        for img_file, text, row, col in puno_options:
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 0)
            option_layout.setSpacing(5)

            if img_file:
                image_widget = QSvgWidget(f"docs/svgs/Modelo Puño/{img_file}")
                image_widget.setFixedSize(80, 60)
            else:
                image_widget = QLabel(text)
                image_widget.setFixedSize(60, 60)
                image_widget.setStyleSheet("border: 1px solid black;")
                image_widget.setAlignment(Qt.AlignCenter)
            
            radio_button = QRadioButton(text)
            self.modelo_puno_button_group.addButton(radio_button)

            option_layout.addWidget(image_widget, alignment=Qt.AlignCenter)
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
            "Valentino L", "Neru", "Royal"
        ]
        for i, option_text in enumerate(simple_cuello_options):
            rb = QRadioButton(option_text)
            self.modelo_cuello_button_group.addButton(rb)
            cuello_grid_layout.addWidget(rb, i % 5, i // 5)

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

        # --- Independent Collar Options ---
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        modelos_cuello_layout.addWidget(line)

        independent_options_layout = QGridLayout()
        modelos_cuello_layout.addLayout(independent_options_layout)

        # Plum
        self.plum_cuello_group = QButtonGroup()
        independent_options_layout.addWidget(QLabel("Plum."), 0, 0)
        rb_plum_fija = QRadioButton("Fija"); self.plum_cuello_group.addButton(rb_plum_fija)
        rb_plum_rever = QRadioButton("Rever."); self.plum_cuello_group.addButton(rb_plum_rever)
        independent_options_layout.addWidget(rb_plum_fija, 0, 1)
        independent_options_layout.addWidget(rb_plum_rever, 0, 2)
        rb_plum_fija.setChecked(True)

        # Bottom Down
        self.bd_cuello_group = QButtonGroup()
        independent_options_layout.addWidget(QLabel("Bottom Down"), 1, 0)
        rb_bd_ext = QRadioButton("Ext"); self.bd_cuello_group.addButton(rb_bd_ext)
        rb_bd_int = QRadioButton("Int"); self.bd_cuello_group.addButton(rb_bd_int)
        independent_options_layout.addWidget(rb_bd_ext, 1, 1)
        independent_options_layout.addWidget(rb_bd_int, 1, 2)
        rb_bd_ext.setChecked(True)

        modelos_cuello_layout.addStretch()

        # --- Otros Detalles ---
        detalles_layout = QGridLayout()
        camisa_layout.addLayout(detalles_layout)

        iniciales_group = QGroupBox("Texto")
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

        saco_layout.addLayout(self.create_saco_section())

        # Pantalon section
        pantalon_group = QGroupBox("MEDIDAS PANTALON")
        content_layout.addWidget(pantalon_group)
        pantalon_layout = self.create_pantalon_section()
        pantalon_group.setLayout(pantalon_layout)

        # Billing section
        billing_section = self.create_billing_section()
        content_layout.addWidget(billing_section)

    def _create_image_option(self, text, image_path, button_group):
        option_container = QWidget()
        option_layout = QVBoxLayout(option_container)
        option_layout.setContentsMargins(0, 0, 0, 0)
        option_layout.setSpacing(5)

        if image_path:
            image_widget = QSvgWidget(image_path)
            image_widget.setFixedSize(100, 100)
        else:
            image_widget = QLabel(text.replace("\\n", "\n"))
            image_widget.setFixedSize(100, 100)
            image_widget.setStyleSheet("border: 1px solid black;")
            image_widget.setAlignment(Qt.AlignCenter)

        radio_button = QRadioButton(text)
        if button_group:
            button_group.addButton(radio_button)

        option_layout.addWidget(image_widget, alignment=Qt.AlignCenter)
        option_layout.addWidget(radio_button, alignment=Qt.AlignCenter)
        return option_container

    def create_saco_section(self):
        saco_section_layout = QVBoxLayout()

        # --- Estilo y Solapa ---
        estilo_solapa_layout = QHBoxLayout()
        saco_section_layout.addLayout(estilo_solapa_layout)

        # Estilo
        estilo_group = QGroupBox("Estilo")
        estilo_solapa_layout.addWidget(estilo_group, 2)
        estilo_main_layout = QVBoxLayout(estilo_group)
        self.estilo_saco_group = QButtonGroup()

        # Images layout
        images_layout = QHBoxLayout()
        images_layout.addStretch()
        img_cruzado = QSvgWidget("docs/svgs/Medidas Saco/Estilo/Cruzado.svg")
        img_cruzado.setFixedSize(100, 100)
        images_layout.addWidget(img_cruzado)
        img_sencillo = QSvgWidget("docs/svgs/Medidas Saco/Estilo/Sencillo.svg")
        img_sencillo.setFixedSize(100, 100)
        images_layout.addWidget(img_sencillo)
        images_layout.addStretch()
        estilo_main_layout.addLayout(images_layout)

        # Radio buttons layout
        radio_layout = QHBoxLayout()
        radio_layout.addStretch()
        rb_cruzado = QRadioButton("Cruzado")
        self.estilo_saco_group.addButton(rb_cruzado)
        radio_layout.addWidget(rb_cruzado)
        rb_sencillo = QRadioButton("Sencillo")
        self.estilo_saco_group.addButton(rb_sencillo)
        radio_layout.addWidget(rb_sencillo)
        radio_layout.addStretch()
        estilo_main_layout.addLayout(radio_layout)

        # Cant. boton layout
        cant_boton_layout = QHBoxLayout()
        cant_boton_layout.addWidget(QLabel("Cant. botón:"))
        self.cant_boton_edit = QLineEdit()
        self.cant_boton_edit.setFixedWidth(100)
        cant_boton_layout.addWidget(self.cant_boton_edit)
        cant_boton_layout.addStretch()
        estilo_main_layout.addLayout(cant_boton_layout)

        # Solapa
        solapa_group = QGroupBox("Solapa")
        estilo_solapa_layout.addWidget(solapa_group, 3)
        solapa_layout = QGridLayout(solapa_group)
        self.solapa_saco_group = QButtonGroup()

        solapa_options = ["Cuadrada", "En punta", "Redonda"]
        for i, opt_text in enumerate(solapa_options):
            opt = self._create_image_option(opt_text, f"docs/svgs/Medidas Saco/Solapa/{opt_text}.svg", self.solapa_saco_group)
            solapa_layout.addWidget(opt, 0, i)
        
        solapa_layout.addWidget(QCheckBox("Ojal solapa"), 1, 0, 1, 3, Qt.AlignCenter)


        # --- Bolsillo Inferior ---
        bolsillo_inf_group = QGroupBox("Bolsillo inferior")
        saco_section_layout.addWidget(bolsillo_inf_group)
        bolsillo_inf_layout = QGridLayout(bolsillo_inf_group)
        self.bolsillo_inf_saco_group = QButtonGroup()

        bolsillo_inf_options = [
            ("Ribete", "Ribete.svg"), 
            ("Aletilla", "Aletilla.svg"), 
            ("Parche", "Parche.svg"), 
            ("Tapa\nRedonda", "Tapa redonda.svg"), 
            ("Tapa\nCuadrada", "Tapa cuadrada.svg"), 
            ("3er\nBolsillo", "3er Bolsillo.svg")
        ]
        for i, (opt_text, img_file) in enumerate(bolsillo_inf_options):
            opt = self._create_image_option(opt_text, f"docs/svgs/Medidas Saco/Bolsillo inferior/{img_file}", self.bolsillo_inf_saco_group)
            bolsillo_inf_layout.addWidget(opt, 0, i)


        # --- Delantero y Abertura ---
        delantero_abertura_layout = QHBoxLayout()
        saco_section_layout.addLayout(delantero_abertura_layout)

        # Delantero
        delantero_group = QGroupBox("Delantero")
        delantero_abertura_layout.addWidget(delantero_group)
        delantero_layout = QHBoxLayout(delantero_group)
        self.delantero_group = QButtonGroup()
        for text in ["RECTO", "CURVO"]:
            rb = QRadioButton(text)
            self.delantero_group.addButton(rb)
            delantero_layout.addWidget(rb)

        # Abertura Espalda
        abertura_group = QGroupBox("Abertura Espalda")
        delantero_abertura_layout.addWidget(abertura_group)
        abertura_layout = QHBoxLayout(abertura_group)
        self.abertura_group = QButtonGroup()
        for text in ["NO", "UNA (1)", "DOS (2)"]:
            rb = QRadioButton(text)
            self.abertura_group.addButton(rb)
            abertura_layout.addWidget(rb)

        # --- Bolsillo Superior ---
        bolsillo_sup_group = QGroupBox("Bolsillo Superior")
        saco_section_layout.addWidget(bolsillo_sup_group)
        bolsillo_sup_layout = QHBoxLayout(bolsillo_sup_group)
        
        si_no_layout = QVBoxLayout()
        si_no_layout.addStretch()
        rb_si_bolsillo = QRadioButton("SI")
        rb_no_bolsillo = QRadioButton("NO")
        si_no_layout.addWidget(rb_si_bolsillo)
        si_no_layout.addWidget(rb_no_bolsillo)
        si_no_layout.addStretch()
        bolsillo_sup_layout.addLayout(si_no_layout)

        self.bolsillo_sup_type_group = QButtonGroup()
        bolsillo_sup_options_container = QWidget()
        bolsillo_sup_options_layout = QHBoxLayout(bolsillo_sup_options_container)

        aletilla_opt = self._create_image_option("ALETILLA", "docs/svgs/Medidas Saco/Bolsillo Superior/Aletilla.svg", self.bolsillo_sup_type_group)
        parche_opt = self._create_image_option("PARCHE", "docs/svgs/Medidas Saco/Bolsillo Superior/Parche.svg", self.bolsillo_sup_type_group)
        bolsillo_sup_options_layout.addWidget(aletilla_opt)
        bolsillo_sup_options_layout.addWidget(parche_opt)
        bolsillo_sup_layout.addWidget(bolsillo_sup_options_container)
        
        self.bolsillo_sup_enable_group = QButtonGroup()
        self.bolsillo_sup_enable_group.addButton(rb_si_bolsillo)
        self.bolsillo_sup_enable_group.addButton(rb_no_bolsillo)

        rb_no_bolsillo.setChecked(True)
        bolsillo_sup_options_container.setEnabled(False)

        def toggle_bolsillo_sup(button):
            if button.text() == "SI":
                bolsillo_sup_options_container.setEnabled(True)
            else:
                bolsillo_sup_options_container.setEnabled(False)
        self.bolsillo_sup_enable_group.buttonClicked.connect(toggle_bolsillo_sup)

        # --- Observaciones y Vendedor ---
        observaciones_group = QGroupBox("Observaciones")
        obs_layout = QVBoxLayout(observaciones_group)
        obs_layout.addWidget(QTextEdit())
        saco_section_layout.addWidget(observaciones_group)

        vendedor_layout = QHBoxLayout()
        vendedor_layout.addWidget(QLabel("Vendedor:"))
        vendedor_layout.addWidget(QLineEdit())
        saco_section_layout.addLayout(vendedor_layout)

        return saco_section_layout

    def create_pantalon_section(self):
        pantalon_section_layout = QHBoxLayout()

        # --- LEFT COLUMN ---
        left_column = QVBoxLayout()

        # Bolsillo Delantero
        bolsillo_del_group = QGroupBox("Bolsillo Delantero")
        left_column.addWidget(bolsillo_del_group)
        bolsillo_del_layout = QGridLayout(bolsillo_del_group)
        self.bolsillo_del_group = QButtonGroup()
        delantero_options = [
            ("Jean #1", "Jean 1.svg"), ("Jean #2", "Jean 2.svg"),("Sesgado #3", "Sesgado 3.svg"),
            ("Ses. T Recta #4", "SES T RECTA 4.svg"),("Ses. T Curva #5", "SES T CURVA 5.svg"),("Allado #6", "Allado 6.svg"),
            ("Redondo #7", "Redondo 7.svg"),("Italiano #8", "Italiano 8.svg"),("Texas #9", "Texas 9.svg"),
            ("Texas #10", "Texas 10.svg"),("Texas #11", "Texas 11.svg"),("Texas #12", "Texas 12.svg")
        ]
        for i, (text, svg) in enumerate(delantero_options):
            opt = self._create_image_option(text, f"docs/svgs/Medidas Pantalon/Bolsillo Delantero/{svg}", self.bolsillo_del_group)
            bolsillo_del_layout.addWidget(opt, i // 6, i % 6)

        # Bolsillo Trasero and Terminado Layout
        trasero_terminado_layout = QHBoxLayout()
        
        bolsillo_tras_group = QGroupBox("Bolsillo Trasero")
        trasero_terminado_layout.addWidget(bolsillo_tras_group)
        bolsillo_tras_layout = QGridLayout(bolsillo_tras_group)
        self.bolsillo_tras_group = QButtonGroup()
        trasero_options = [
            ("Tapa #1", "Tapa 1.svg"),("Tapa #2", "Tapa 2.svg"),("Tapa #3", "Tapa 3.svg"),
            ("Tapa #4", "Tapa 4.svg"),("Tapa #5", "Tapa 5.svg"),("Ribete", "Ribete.svg"),
            ("Aletilla", "Aletilla.svg"),("Con Oreja", "Con oreja.svg")
        ]
        for i, (text, svg) in enumerate(trasero_options):
            opt = self._create_image_option(text, f"docs/svgs/Medidas Pantalon/Bolsillo Trasero/{svg}", self.bolsillo_tras_group)
            bolsillo_tras_layout.addWidget(opt, i // 4, i % 4)
        
        terminado_group = QGroupBox("Terminado Bolsillo Trasero")
        trasero_terminado_layout.addWidget(terminado_group)
        terminado_layout = QGridLayout(terminado_group)

        # Boton row
        terminado_layout.addWidget(QLabel("BOTON"), 0, 0)
        self.terminado_boton_group = QButtonGroup()
        for j, opt_text in enumerate(["Izq", "Der", "NO"]):
            rb = QRadioButton(opt_text)
            self.terminado_boton_group.addButton(rb)
            terminado_layout.addWidget(rb, 0, j + 1)
        
        # Oreja row
        terminado_layout.addWidget(QLabel("OREJA"), 1, 0)
        self.terminado_oreja_group = QButtonGroup()
        for j, opt_text in enumerate(["Izq", "Der", "NO"]):
            rb = QRadioButton(opt_text)
            self.terminado_oreja_group.addButton(rb)
            terminado_layout.addWidget(rb, 1, j + 1)
            
        chk_parche = QCheckBox("PARCHE")
        terminado_layout.addWidget(chk_parche, 2, 0)
        terminado_layout.addWidget(QLabel("MOD #:"), 2, 1)
        edit_mod = QLineEdit()
        edit_mod.setEnabled(False)
        chk_parche.toggled.connect(edit_mod.setEnabled)
        terminado_layout.addWidget(edit_mod, 2, 2, 1, 2)

        left_column.addLayout(trasero_terminado_layout)

        # --- RIGHT COLUMN ---
        right_column = QVBoxLayout()
        
        # Medidas
        medidas_pantalon_layout = QGridLayout()
        pantalon_fields = ["Cintura", "Base", "Largo", "Pierna", "Rodilla", "Bota", "Tiro", "CONT. T"]
        for i, field in enumerate(pantalon_fields):
            medidas_pantalon_layout.addWidget(QLabel(field), 0, i, alignment=Qt.AlignCenter)
            medidas_pantalon_layout.addWidget(QLineEdit(), 1, i)
        right_column.addLayout(medidas_pantalon_layout)

        # Pretina
        pretina_group = QGroupBox("Pretina")
        right_column.addWidget(pretina_group)
        pretina_layout = QHBoxLayout(pretina_group)
        pretina_modelos_group = QGroupBox()
        pretina_modelos_layout = QGridLayout(pretina_modelos_group)
        self.pretina_modelos_group = QButtonGroup()
        pretina_options = [
            ("Recta", "Recta.svg"), ("Cruzada\nCurva", "Cruzada curva.svg"),
            ("Cruzada\nRecta", "Cruzada recta.svg"), ("Cruzada\nPunta", "Cruzada punta.svg")
        ]
        for i, (text, svg) in enumerate(pretina_options):
             opt = self._create_image_option(text, f"docs/svgs/Medidas Pantalon/Pretina/{svg}", self.pretina_modelos_group)
             pretina_modelos_layout.addWidget(opt, 0, i)
        pretina_layout.addWidget(pretina_modelos_group)
        pretina_opts_group = QGroupBox()
        pretina_opts_layout = QVBoxLayout(pretina_opts_group)
        pretina_opts_layout.addWidget(QCheckBox("BOTON"))
        pretina_opts_layout.addWidget(QCheckBox("GANCHO"))
        pasadores_group = QGroupBox("PASADORES")
        pasadores_layout = QHBoxLayout(pasadores_group)
        self.pasadores_group = QButtonGroup()
        for text in ["NO", "Normal", "Dobles"]:
            rb = QRadioButton(text)
            self.pasadores_group.addButton(rb)
            pasadores_layout.addWidget(rb)
        pretina_opts_layout.addWidget(pasadores_group)
        pretina_layout.addWidget(pretina_opts_group)

        # Bottom Right Layout
        bottom_right_layout = QHBoxLayout()
        right_column.addLayout(bottom_right_layout)
        
        side_panel_group = QGroupBox()
        bottom_right_layout.addWidget(side_panel_group)
        side_panel = QGridLayout(side_panel_group)

        forrado_group = QGroupBox("Forrado")
        forrado_layout = QGridLayout(forrado_group)
        side_panel.addWidget(forrado_group, 0, 0, 2, 1)
        rb_forrado_si = QRadioButton("SI"); rb_forrado_no = QRadioButton("NO")
        forrado_layout.addWidget(rb_forrado_si, 0, 0); forrado_layout.addWidget(rb_forrado_no, 0, 1)
        forrado_options_widget = QWidget()
        forrado_options_layout = QGridLayout(forrado_options_widget)
        self.forrado_todo_mitad_group = QButtonGroup(); self.forrado_frente_trasero_group = QButtonGroup()
        for r, (text1, text2) in enumerate([("TODO", "MITAD"), ("Frente", "Trasero")]):
            rb1 = QRadioButton(text1); rb2 = QRadioButton(text2)
            if r == 0: self.forrado_todo_mitad_group.addButton(rb1); self.forrado_todo_mitad_group.addButton(rb2)
            else: self.forrado_frente_trasero_group.addButton(rb1); self.forrado_frente_trasero_group.addButton(rb2)
            forrado_options_layout.addWidget(rb1, r, 0); forrado_options_layout.addWidget(rb2, r, 1)
        forrado_layout.addWidget(forrado_options_widget, 1, 0, 1, 2)
        forrado_options_widget.setEnabled(False)
        rb_forrado_si.toggled.connect(forrado_options_widget.setEnabled)
        rb_forrado_no.setChecked(True)
        
        especial_group = QGroupBox("Especial"); especial_layout = QVBoxLayout(especial_group)
        side_panel.addWidget(especial_group, 0, 1)
        especial_layout.addWidget(QLineEdit()); especial_layout.addWidget(QCheckBox("Relojera"))
        
        bota_group = QGroupBox("Bota"); bota_layout = QVBoxLayout(bota_group)
        side_panel.addWidget(bota_group, 1, 1)
        for text in ["Lisa", "Voltea", "Pespun."]: bota_layout.addWidget(QRadioButton(text))
            
        estilo_del_group = QGroupBox("Estilo Delantero"); estilo_del_layout = QVBoxLayout(estilo_del_group)
        side_panel.addWidget(estilo_del_group, 2, 0, 1, 2)
        estilo_del_h_layout = QHBoxLayout(); estilo_del_layout.addLayout(estilo_del_h_layout)
        for text in ["Liso", "Prenses", "Fuelle"]: estilo_del_h_layout.addWidget(QRadioButton(text))

        obs_vend_layout = QVBoxLayout()
        bottom_right_layout.addLayout(obs_vend_layout)
        observaciones_group = QGroupBox("Observaciones"); obs_vend_layout.addWidget(observaciones_group)
        obs_layout = QVBoxLayout(observaciones_group); obs_layout.addWidget(QTextEdit())
        vendedor_layout = QHBoxLayout(); obs_vend_layout.addLayout(vendedor_layout)
        vendedor_layout.addWidget(QLabel("Vendedor:")); vendedor_layout.addWidget(QLineEdit())

        pantalon_section_layout.addLayout(left_column, 2)
        pantalon_section_layout.addLayout(right_column, 3)

        return pantalon_section_layout

    def create_billing_section(self):
        billing_group = QGroupBox("ORDEN DE TRABAJO")
        main_layout = QVBoxLayout(billing_group)

        # Header
        header_layout = QHBoxLayout()
        
        logo_label = QLabel()
        pixmap = QPixmap("modiapp/assets/Logo.png")
        logo_label.setPixmap(pixmap.scaledToWidth(200))
        header_layout.addWidget(logo_label)
        
        company_info_text = """
        <b>Calle 9 No. 55 - 13 2do piso</b><br>
        Tel.: 389 8921 - Cel.: 315 479 6076<br>
        E-mail: ferdinand.sartorial@gmail.com<br>
        www.ferdinandsartorial.com<br>
        Cali - Colombia
        """
        company_label = QLabel(company_info_text)
        header_layout.addWidget(company_label)
        header_layout.addStretch()

        order_info_layout = QVBoxLayout()
        order_info_layout.addWidget(QLabel("<b>ORDEN TRABAJO</b>"), alignment=Qt.AlignRight)
        order_info_layout.addWidget(QLabel("<b>N° 0000</b>"), alignment=Qt.AlignRight)
        order_info_layout.addWidget(QLabel("<b>NO VALIDO COMO FACTURA</b>"), alignment=Qt.AlignRight)
        header_layout.addLayout(order_info_layout)
        main_layout.addLayout(header_layout)
        
        # Top Row (Dates, Client Info, Financials)
        top_row_layout = QHBoxLayout()
        
        # Client and Dates
        client_date_layout = QVBoxLayout()
        
        date_sm_layout = QHBoxLayout()
        # Dates
        fecha_orden_group = QGroupBox("Fecha Orden")
        fecha_orden_layout = QHBoxLayout(fecha_orden_group)
        self.billing_fecha_orden_label = QLabel()
        fecha_orden_layout.addWidget(self.billing_fecha_orden_label)
        date_sm_layout.addWidget(fecha_orden_group)

        fecha_entrega_group = QGroupBox("Fecha Entrega")
        fecha_entrega_layout = QHBoxLayout(fecha_entrega_group)
        self.billing_fecha_entrega_label = QLabel()
        fecha_entrega_layout.addWidget(self.billing_fecha_entrega_label)
        date_sm_layout.addWidget(fecha_entrega_group)
        
        # SM, SC, AG, AC
        sm_sc_group = QGroupBox()
        sm_sc_layout = QGridLayout(sm_sc_group)
        for i, text in enumerate(["SM", "SC", "AG", "AC"]):
            sm_sc_layout.addWidget(QLabel(text), 0, i, alignment=Qt.AlignCenter)
            sm_sc_layout.addWidget(QLineEdit(), 1, i)
        date_sm_layout.addWidget(sm_sc_group)
        
        client_date_layout.addLayout(date_sm_layout)

        # Client info inputs
        client_info_group = QGroupBox()
        client_info_layout = QGridLayout(client_info_group)
        client_info_layout.addWidget(QLabel("Cliente:"), 0, 0); self.billing_cliente_label = QLabel(); client_info_layout.addWidget(self.billing_cliente_label, 0, 1, 1, 5)
        client_info_layout.addWidget(QLabel("Dirección:"), 1, 0); client_info_layout.addWidget(QLineEdit(), 1, 1, 1, 5)
        client_info_layout.addWidget(QLabel("Teléfono:"), 2, 0); client_info_layout.addWidget(QLineEdit(), 2, 1)
        client_info_layout.addWidget(QLabel("C.C.:"), 2, 2); client_info_layout.addWidget(QLineEdit(), 2, 3)
        client_date_layout.addWidget(client_info_group)
        
        top_row_layout.addLayout(client_date_layout)

        # Financials
        financial_group = QGroupBox()
        financial_layout = QGridLayout(financial_group)
        financial_layout.addWidget(QLabel("VALOR ORDEN"), 0, 0); financial_layout.addWidget(QLabel("ABONO"), 0, 1); financial_layout.addWidget(QLabel("SALDO"), 0, 2)
        self.valor_orden_edit = QLineEdit(); self.abono_edit = QLineEdit(); self.saldo_label = QLabel("$ 0")
        self.valor_orden_edit.setValidator(QIntValidator())
        self.abono_edit.setValidator(QIntValidator())
        financial_layout.addWidget(self.valor_orden_edit, 1, 0); financial_layout.addWidget(self.abono_edit, 1, 1); financial_layout.addWidget(self.saldo_label, 1, 2, alignment=Qt.AlignCenter)
        top_row_layout.addWidget(financial_group)
        
        main_layout.addLayout(top_row_layout)
        
        # Reference Grid
        ref_table = QTableWidget(6, 3)
        ref_table.setHorizontalHeaderLabels(["Ref.", "Color", "Valor"])
        ref_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(ref_table)
        
        # Connect signals
        self.cliente_name_edit.textChanged.connect(self.billing_cliente_label.setText)
        self.fecha_orden_edit.dateChanged.connect(lambda date: self.billing_fecha_orden_label.setText(date.toString("dd/MM/yyyy")))
        self.fecha_entrega_edit.dateChanged.connect(lambda date: self.billing_fecha_entrega_label.setText(date.toString("dd/MM/yyyy")))
        self.valor_orden_edit.textChanged.connect(self.update_saldo)
        self.abono_edit.textChanged.connect(self.update_saldo)

        # Initial values
        self.billing_fecha_orden_label.setText(QDate.currentDate().toString("dd/MM/yyyy"))
        self.billing_fecha_entrega_label.setText(QDate.currentDate().toString("dd/MM/yyyy"))
        
        return billing_group

    def update_saldo(self):
        valor = int(self.valor_orden_edit.text()) if self.valor_orden_edit.text() else 0
        abono = int(self.abono_edit.text()) if self.abono_edit.text() else 0
        saldo = valor - abono
        self.saldo_label.setText(f"$ {saldo:,}")

class QIntValidator(QValidator):
    def validate(self, input, pos):
        if not input or input.isdigit():
            return (QValidator.Acceptable, input, pos)
        return (QValidator.Invalid, input, pos)

    def fixup(self, input):
        return "".join(filter(str.isdigit, input))

    def show_create_order_screen(self):
        self.stacked_widget.setCurrentWidget(self.create_order_screen) 