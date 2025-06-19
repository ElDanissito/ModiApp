from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QGroupBox, QScrollArea, QFrame,
                             QGridLayout, QSizePolicy)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
import os

class ViewOrderScreen(QWidget):
    def __init__(self, db, order_id):
        super().__init__()
        self.db = db
        self.order_id = order_id
        self.order_data = self.db.get_order_details(order_id)
        self.svg_base_path = "docs/svgs"
        
        self.init_ui()
    
    def get_svg_path(self, section, field, value):
        """Get the appropriate SVG path based on section, field and value"""
        if not value or value.lower() == 'no':
            return None
            
        # Mapeo completo de todos los campos con sus SVGs
        svg_paths = {
            'camisa': {
                'modelo_espalda': {
                    'Tableta': f"{self.svg_base_path}/Modelo Espalda/Tableta_1.svg",
                    'Prenses': f"{self.svg_base_path}/Modelo Espalda/Prenses_2.svg",
                    'Fuelle': f"{self.svg_base_path}/Modelo Espalda/Fuelle_3.svg",
                    'Doble Tableta': f"{self.svg_base_path}/Modelo Espalda/Doble Tableta_4.svg",
                    'Pinzas': f"{self.svg_base_path}/Modelo Espalda/Pinzas_5.svg",
                    'Lisa': f"{self.svg_base_path}/Modelo Espalda/Lisa_6.svg"
                },
                'modelo_bolsillo': {
                    'Fuelle #11': f"{self.svg_base_path}/Modelo Bolsillo/1.svg",
                    'En punta con Tapa #5': f"{self.svg_base_path}/Modelo Bolsillo/2.svg",
                    'En Punta Imitación Tapa #8': f"{self.svg_base_path}/Modelo Bolsillo/3.svg",
                    'En Punta Liso #1': f"{self.svg_base_path}/Modelo Bolsillo/4.svg",
                    'En Punta con Dobles #4': f"{self.svg_base_path}/Modelo Bolsillo/5.svg",
                    'Diagonal Liso #2': f"{self.svg_base_path}/Modelo Bolsillo/6.svg",
                    'Diagonal Tableta #2': f"{self.svg_base_path}/Modelo Bolsillo/7.svg",
                    'Diagonal con Tapa #13': f"{self.svg_base_path}/Modelo Bolsillo/8.svg",
                    'Redondo Liso #7': f"{self.svg_base_path}/Modelo Bolsillo/9.svg",
                    'Redondo con Tapa #5': f"{self.svg_base_path}/Modelo Bolsillo/10.svg",
                    'Redondo Corte Despuntado #9': f"{self.svg_base_path}/Modelo Bolsillo/11.svg",
                    'Redondo Oreja con Botón #10': f"{self.svg_base_path}/Modelo Bolsillo/12.svg",
                    'Cuadrado #3': f"{self.svg_base_path}/Modelo Bolsillo/13.svg"
                },
                'modelo_puño': {
                    'R.D': f"{self.svg_base_path}/Modelo Puño/RD.svg",
                    'R.A': f"{self.svg_base_path}/Modelo Puño/RA.svg",
                    'PUNTA': f"{self.svg_base_path}/Modelo Puño/PUNTA.svg",
                    'D.USO': f"{self.svg_base_path}/Modelo Puño/D USO.svg",
                    'R.A.2B': f"{self.svg_base_path}/Modelo Puño/RA2B.svg",
                    'MAN': f"{self.svg_base_path}/Modelo Puño/MAN.svg",
                    'DISEÑO': f"{self.svg_base_path}/Modelo Puño/DISEÑO.svg",
                    'MANGA CORTA': f"{self.svg_base_path}/Modelo Puño/MANGA_CORTA.svg"
                }
            },
            'saco': {
                'modelo_chaleco': {
                    'Chaleco': f"{self.svg_base_path}/Medidas Saco/Modelo chaleco/Chaleco.svg"
                },
                'bolsillo_superior': {
                    'Aletilla': f"{self.svg_base_path}/Medidas Saco/Bolsillo Superior/Aletilla.svg",
                    'Parche': f"{self.svg_base_path}/Medidas Saco/Bolsillo Superior/Parche.svg"
                },
                'bolsillo_inferior': {
                    '3er Bolsillo': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/3er Bolsillo.svg",
                    'Aletilla': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Aletilla.svg",
                    'Parche': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Parche.svg",
                    'Ribete': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Ribete.svg",
                    'Tapa Cuadrada': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Tapa cuadrada.svg",
                    'Tapa Redonda': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Tapa redonda.svg"
                },
                'solapa': {
                    'Cuadrada': f"{self.svg_base_path}/Medidas Saco/Solapa/Cuadrada.svg",
                    'En punta': f"{self.svg_base_path}/Medidas Saco/Solapa/En punta.svg",
                    'Redonda': f"{self.svg_base_path}/Medidas Saco/Solapa/Redonda.svg"
                },
                'estilo': {
                    'Cruzado': f"{self.svg_base_path}/Medidas Saco/Estilo/Cruzado.svg",
                    'Sencillo': f"{self.svg_base_path}/Medidas Saco/Estilo/Sencillo.svg"
                }
            },
            'pantalon': {
                'bolsillo_delantero': {
                    'Jean #1': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Jean 1.svg",
                    'Jean #2': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Jean 2.svg",
                    'Sesgado #3': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Sesgado 3.svg",
                    'Ses. T Recta #4': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/SES T RECTA 4.svg",
                    'Ses. T Curva #5': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/SES T CURVA 5.svg",
                    'Allado #6': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Allado 6.svg",
                    'Redondo #7': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Redondo 7.svg",
                    'Italiano #8': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Italiano 8.svg",
                    'Texas #9': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 9.svg",
                    'Texas #10': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 10.svg",
                    'Texas #11': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 11.svg",
                    'Texas #12': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 12.svg"
                },
                'bolsillo_trasero': {
                    'Tapa #1': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 1.svg",
                    'Tapa #2': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 2.svg",
                    'Tapa #3': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 3.svg",
                    'Tapa #4': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 4.svg",
                    'Tapa #5': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 5.svg",
                    'Ribete': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Ribete.svg",
                    'Aletilla': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Aletilla.svg",
                    'Con Oreja': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Con oreja.svg"
                },
                'pretina': {
                    'Recta': f"{self.svg_base_path}/Medidas pantalon/Pretina/Recta.svg",
                    'Cruzada Curva': f"{self.svg_base_path}/Medidas pantalon/Pretina/Cruzada curva.svg",
                    'Cruzada Recta': f"{self.svg_base_path}/Medidas pantalon/Pretina/Cruzada recta.svg",
                    'Cruzada Punta': f"{self.svg_base_path}/Medidas pantalon/Pretina/Cruzada punta.svg"
                }
            }
        }
        
        try:
            # Normalizar el valor para la búsqueda
            normalized_value = value.strip().replace('\n', ' ')
            # Buscar en el mapeo
            if section in svg_paths and field in svg_paths[section]:
                for key, path in svg_paths[section][field].items():
                    if key.lower() == normalized_value.lower():
                        return path
            return None
        except (KeyError, AttributeError):
            return None
        
    def create_svg_widget(self, svg_path, size=(300, 300)):
        """Create and return an SVG widget if the path exists"""
        if svg_path and os.path.exists(svg_path):
            svg_widget = QSvgWidget(svg_path)
            svg_widget.setFixedSize(size[0], size[1])
            return svg_widget
        return None
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Ver Orden")
        self.resize(1200, 800)
        main_layout = QVBoxLayout(self)
        
        # Header with Logo and Back Button
        header_layout = QHBoxLayout()
        
        back_button = QPushButton("← Volver")
        back_button.clicked.connect(self.close)
        header_layout.addWidget(back_button)
        
        logo_label = QLabel()
        pixmap = QPixmap("modiapp/assets/Logo.png")
        logo_label.setPixmap(pixmap.scaledToWidth(250))
        header_layout.addWidget(logo_label)
        header_layout.addStretch()
        
        main_layout.addLayout(header_layout)
        
        # Order Info
        order_info = self.order_data['order']
        info_group = QGroupBox("Información de la Orden")
        info_layout = QGridLayout()
        
        info_layout.addWidget(QLabel("<b>Número de Orden:</b>"), 0, 0)
        info_layout.addWidget(QLabel(order_info['order_number']), 0, 1)
        
        info_layout.addWidget(QLabel("<b>Cliente:</b>"), 1, 0)
        info_layout.addWidget(QLabel(order_info['client_name']), 1, 1)
        
        info_layout.addWidget(QLabel("<b>Fecha de Orden:</b>"), 2, 0)
        info_layout.addWidget(QLabel(order_info['order_date']), 2, 1)
        
        info_layout.addWidget(QLabel("<b>Fecha de Entrega:</b>"), 3, 0)
        info_layout.addWidget(QLabel(order_info['delivery_date']), 3, 1)
        
        info_layout.addWidget(QLabel("<b>Estado:</b>"), 4, 0)
        info_layout.addWidget(QLabel(order_info['status']), 4, 1)
        
        if order_info.get('vendedor'):
            info_layout.addWidget(QLabel("<b>Vendedor:</b>"), 5, 0)
            info_layout.addWidget(QLabel(order_info['vendedor']), 5, 1)
        
        info_group.setLayout(info_layout)
        main_layout.addWidget(info_group)
        
        # Financial Info
        financial_group = QGroupBox("Información Financiera")
        financial_layout = QGridLayout()
        
        financial_layout.addWidget(QLabel("<b>Valor de la Orden:</b>"), 0, 0)
        financial_layout.addWidget(QLabel(f"$ {order_info['order_value']:,}"), 0, 1)
        
        financial_layout.addWidget(QLabel("<b>Abono:</b>"), 1, 0)
        financial_layout.addWidget(QLabel(f"$ {order_info['deposit']:,}"), 1, 1)
        
        saldo = order_info['order_value'] - order_info['deposit']
        financial_layout.addWidget(QLabel("<b>Saldo:</b>"), 2, 0)
        financial_layout.addWidget(QLabel(f"$ {saldo:,}"), 2, 1)
        
        financial_group.setLayout(financial_layout)
        main_layout.addWidget(financial_group)
        
        # References
        if self.order_data['references']:
            references_group = QGroupBox("Referencias")
            references_layout = QGridLayout()
            
            for i, ref in enumerate(self.order_data['references']):
                references_layout.addWidget(QLabel(f"<b>Ref {i+1}:</b>"), i, 0)
                references_layout.addWidget(QLabel(ref['reference']), i, 1)
                references_layout.addWidget(QLabel(f"<b>Color:</b>"), i, 2)
                references_layout.addWidget(QLabel(ref['color']), i, 3)
                references_layout.addWidget(QLabel(f"<b>Valor:</b>"), i, 4)
                references_layout.addWidget(QLabel(f"$ {ref['value']:,}"), i, 5)
            
            references_group.setLayout(references_layout)
            main_layout.addWidget(references_group)
        
        # Details Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        details_widget = QWidget()
        details_layout = QVBoxLayout(details_widget)
        
        # Add measurement sections with their corresponding images
        if 'camisa' in self.order_data['details']:
            camisa_section = self.create_camisa_section()
            details_layout.addWidget(camisa_section)
        
        if 'saco' in self.order_data['details']:
            saco_section = self.create_saco_section()
            details_layout.addWidget(saco_section)
        
        if 'pantalon' in self.order_data['details']:
            pantalon_section = self.create_pantalon_section()
            details_layout.addWidget(pantalon_section)
        
        details_layout.addStretch()
        scroll.setWidget(details_widget)
        main_layout.addWidget(scroll, 1)
        
        # Add some spacing at the bottom
        main_layout.addStretch()
    
    def create_camisa_section(self):
        """Create the camisa section with all details"""
        section_data = self.order_data['details'].get('camisa', {})
        section_group = QGroupBox("MEDIDAS CAMISA")
        section_layout = QVBoxLayout(section_group)
        
        # Main layout for all content
        main_content_layout = QHBoxLayout()

        # Left side layout
        left_layout = QVBoxLayout()
        
        # Medidas Básicas
        medidas_group = QGroupBox("Medidas")
        medidas_layout = QGridLayout(medidas_group)
        
        medidas = ['Cuello', 'Espalda', 'Hombro', 'Manga x Cont.', 'Largo', 'Cont. manga', 'Pecho', 'Cintura', 'Cadera']
        row, col = 0, 0
        for medida in medidas:
            if medida in section_data and section_data[medida]:
                medidas_layout.addWidget(QLabel(f"<b>{medida}:</b>"), row, col * 2)
                medidas_layout.addWidget(QLabel(section_data[medida]), row, col * 2 + 1)
                col = (col + 1) % 4
                if col == 0: row += 1
        
        left_layout.addWidget(medidas_group)

        # Prenda, Empaque, Contextura, Vendedor
        other_details_layout = QGridLayout()
        
        if section_data.get('Prenda'):
            other_details_layout.addWidget(QLabel("<b>Prenda:</b>"), 0, 0)
            other_details_layout.addWidget(QLabel(section_data['Prenda']), 0, 1)

        if section_data.get('Empaque'):
            other_details_layout.addWidget(QLabel("<b>Empaque:</b>"), 0, 2)
            other_details_layout.addWidget(QLabel(section_data['Empaque']), 0, 3)

        ctx_espalda = section_data.get('contextura_fisica_espalda')
        ctx_abdomen = section_data.get('contextura_fisica_abdomen')
        if ctx_espalda or ctx_abdomen:
            ctx_group = QGroupBox("Contextura Física")
            ctx_layout = QHBoxLayout(ctx_group)
            if ctx_espalda:
                ctx_layout.addWidget(QLabel(f"<b>Espalda:</b> {ctx_espalda}"))
            if ctx_abdomen:
                ctx_layout.addWidget(QLabel(f"<b>Abdomen:</b> {ctx_abdomen}"))
            other_details_layout.addWidget(ctx_group, 1, 0, 1, 2)

        if section_data.get('vendedor'):
            other_details_layout.addWidget(QLabel("<b>Vendedor:</b>"), 1, 2)
            other_details_layout.addWidget(QLabel(section_data['vendedor']), 1, 3)

        left_layout.addLayout(other_details_layout)
        
        # Texto Section
        texto_fields = ['texto_iniciales', 'texto_color', 'texto_tipo', 'texto_bol', 'texto_fre', 'texto_puñ']
        if any(field in section_data and section_data.get(field) for field in texto_fields):
            texto_group = QGroupBox("Texto")
            texto_layout = QGridLayout(texto_group)
            row, col = 0, 0
            for field in texto_fields:
                if section_data.get(field):
                    label = field.replace('texto_', '').title()
                    texto_layout.addWidget(QLabel(f"<b>{label}:</b>"), row, col * 2)
                    texto_layout.addWidget(QLabel(section_data[field]), row, col * 2 + 1)
                    col = (col + 1) % 3
                    if col == 0: row += 1
            left_layout.addWidget(texto_group)

        # Falda Section
        falda_fields = ['falda_color', 'falda_marip', 'falda_r_abert']
        if any(field in section_data and section_data[field] for field in falda_fields):
            falda_group = QGroupBox("Falda")
            falda_layout = QGridLayout(falda_group)
            for i, field in enumerate(falda_fields):
                if section_data.get(field):
                    label = field.replace('falda_', '').replace('_', ' ').title()
                    falda_layout.addWidget(QLabel(f"<b>{label}:</b>"), 0, i*2)
                    falda_layout.addWidget(QLabel(section_data[field]), 0, i*2 + 1)
            left_layout.addWidget(falda_group)

        main_content_layout.addLayout(left_layout)
        
        # Right side layout (models)
        right_layout = QVBoxLayout()
        
        # Modelo Espalda
        espalda_group = QGroupBox("Modelo Espalda")
        espalda_layout = QVBoxLayout(espalda_group)
        espalda_value = section_data.get('modelo_espalda', '')
        
        if espalda_value and espalda_value.lower() != 'no':
            espalda_svg_path = self.get_svg_path('camisa', 'modelo_espalda', espalda_value)
            espalda_svg = self.create_svg_widget(espalda_svg_path, (150, 150))
            if espalda_svg:
                espalda_layout.addWidget(espalda_svg, alignment=Qt.AlignmentFlag.AlignCenter)
            espalda_layout.addWidget(QLabel(espalda_value), alignment=Qt.AlignmentFlag.AlignCenter)
        else:
            espalda_layout.addWidget(QLabel("NO"), alignment=Qt.AlignmentFlag.AlignCenter)
        
        if section_data.get('modelo_espalda_prespuente'):
            espalda_layout.addWidget(QLabel(f"<b>Prespuente:</b> {section_data['modelo_espalda_prespuente']}"))
        if section_data.get('modelo_espalda_pechera') == 'True':
            espalda_layout.addWidget(QLabel("<b>Pechera:</b> Sí"))
        if section_data.get('modelo_espalda_tapa_boton') == 'True':
            espalda_layout.addWidget(QLabel("<b>Tapa Botón:</b> Sí"))

        right_layout.addWidget(espalda_group)
        
        # Modelo Bolsillo
        bolsillo_group = QGroupBox("Modelo Bolsillo")
        bolsillo_layout = QVBoxLayout(bolsillo_group)
        bolsillo_value = section_data.get('modelo_bolsillo', '')
        bolsillo_value = bolsillo_value.replace('\\n', ' ')
        if bolsillo_value and bolsillo_value.lower() != 'no':
            bolsillo_svg_path = self.get_svg_path('camisa', 'modelo_bolsillo', bolsillo_value)
            bolsillo_svg = self.create_svg_widget(bolsillo_svg_path, (100, 100))
            if bolsillo_svg:
                bolsillo_layout.addWidget(bolsillo_svg, alignment=Qt.AlignmentFlag.AlignCenter)
            bolsillo_layout.addWidget(QLabel(bolsillo_value), alignment=Qt.AlignmentFlag.AlignCenter)
            
            if section_data.get('lado_bolsillo'):
                bolsillo_layout.addWidget(QLabel(f"<b>Lado:</b> {section_data['lado_bolsillo']}"))
            if section_data.get('cantidad_bolsillo'):
                bolsillo_layout.addWidget(QLabel(f"<b>Cantidad:</b> {section_data['cantidad_bolsillo']}"))
        else:
            bolsillo_layout.addWidget(QLabel("NO"), alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(bolsillo_group)
        
        # Modelo Puño
        puno_group = QGroupBox("Modelo Puño")
        puno_layout = QVBoxLayout(puno_group)
        puno_value = section_data.get('modelo_puno', '')
        if puno_value and puno_value.lower() != 'no':
            puno_svg_path = self.get_svg_path('camisa', 'modelo_puño', puno_value)
            puno_svg = self.create_svg_widget(puno_svg_path, (100, 100))
            if puno_svg:
                puno_layout.addWidget(puno_svg, alignment=Qt.AlignmentFlag.AlignCenter)
            puno_layout.addWidget(QLabel(puno_value), alignment=Qt.AlignmentFlag.AlignCenter)
            
            if section_data.get('textura_puno'):
                puno_layout.addWidget(QLabel(f"<b>Textura:</b> {section_data['textura_puno']}"))
            if section_data.get('ancho_cms_puno'):
                puno_layout.addWidget(QLabel(f"<b>Ancho:</b> {section_data['ancho_cms_puno']} cm"))
        else:
            puno_layout.addWidget(QLabel("NO"), alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(puno_group)

        # Modelo Cuello
        cuello_group = QGroupBox("Modelo Cuello")
        cuello_layout = QVBoxLayout(cuello_group)
        cuello_value = section_data.get('modelo_cuello', '')
        if cuello_value and cuello_value.lower() != 'no':
            cuello_layout.addWidget(QLabel(cuello_value), alignment=Qt.AlignmentFlag.AlignCenter)
            
            if section_data.get('textura_cuello'):
                cuello_layout.addWidget(QLabel(f"<b>Textura:</b> {section_data['textura_cuello']}"))
            if section_data.get('plum_cuello'):
                cuello_layout.addWidget(QLabel(f"<b>Plum:</b> {section_data['plum_cuello']}"))
            if section_data.get('bottom_down_cuello'):
                cuello_layout.addWidget(QLabel(f"<b>Bottom Down:</b> {section_data['bottom_down_cuello']}"))
        else:
            cuello_layout.addWidget(QLabel("NO"), alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(cuello_group)

        main_content_layout.addLayout(right_layout)
        section_layout.addLayout(main_content_layout)
        
        # Observaciones
        if section_data.get('observaciones'):
            obs_group = QGroupBox("Observaciones")
            obs_layout = QVBoxLayout(obs_group)
            obs_layout.addWidget(QLabel(section_data['observaciones']))
            section_layout.addWidget(obs_group)
        
        return section_group
    
    def create_saco_section(self):
        """Create the saco section with all details"""
        section_data = self.order_data['details']['saco']
        section_group = QGroupBox("MEDIDAS SACO")
        section_layout = QVBoxLayout()
        
        main_grid = QGridLayout()

        # Medidas Saco
        medidas_group = self.create_data_group(
            "Medidas Saco",
            section_data,
            ['Talle', 'Largo', '1/2 espalda', 'Hombro', 'Manga', 'Pecho', 'Cintura', 'Cadera']
        )
        main_grid.addWidget(medidas_group, 0, 0)
        
        # Estilo
        estilo_group = self.create_image_display_group(
            "Estilo", 'saco', 'estilo', section_data,
            field_name='Estilo',
            additional_fields={'Cant. Botón': 'cantidad_boton'}
        )
        main_grid.addWidget(estilo_group, 0, 1)

        # Solapa
        solapa_group = self.create_image_display_group(
            "Solapa", 'saco', 'solapa', section_data,
            field_name='Solapa',
            additional_fields={'Ojal Solapa': 'ojal_solapa'}
        )
        main_grid.addWidget(solapa_group, 0, 2)
        
        # Bolsillo Inferior
        bolsillo_inf_group = self.create_image_display_group(
            "Bolsillo Inferior", 'saco', 'bolsillo_inferior', section_data,
            field_name='Bolsillo Inferior'
        )
        main_grid.addWidget(bolsillo_inf_group, 1, 0)

        # Bolsillo Superior
        bolsillo_sup_group = self.create_image_display_group(
            "Bolsillo Superior", 'saco', 'bolsillo_superior', section_data,
            field_name='Bolsillo superior'
        )
        main_grid.addWidget(bolsillo_sup_group, 1, 1)

        # Delantero
        delantero_group = self.create_data_group("Delantero", section_data, ['Delantero'])
        main_grid.addWidget(delantero_group, 1, 2)

        # Abertura
        abertura_group = self.create_data_group("Abertura", section_data, ['Abertura'])
        main_grid.addWidget(abertura_group, 2, 0)

        # Modelo Chaleco
        chaleco_group = self.create_image_display_group(
            "Modelo Chaleco", 'saco', 'modelo_chaleco', section_data,
            field_name='Modelo chaleco',
            additional_fields={
                'Diagonal Pecho': 'chaleco_diagonal_pecho',
                'Centro': 'chaleco_centro',
                'Largo Espalda': 'chaleco_largo_espalda',
                'Observaciones': 'observaciones_chaleco'
            }
        )
        main_grid.addWidget(chaleco_group, 2, 1)

        # Vendedor
        vendedor_group = self.create_data_group("Vendedor", section_data, ['vendedor'])
        main_grid.addWidget(vendedor_group, 2, 2)
        
        section_layout.addLayout(main_grid)

        # Observaciones Saco
        if section_data.get('observaciones'):
            obs_group = QGroupBox("Observaciones Saco")
            obs_layout = QVBoxLayout()
            obs_label = QLabel(section_data['observaciones'])
            obs_label.setWordWrap(True)
            obs_layout.addWidget(obs_label)
            obs_group.setLayout(obs_layout)
            section_layout.addWidget(obs_group)

        section_group.setLayout(section_layout)
        return section_group

    def create_data_group(self, title, data, fields):
        group = QGroupBox(title)
        layout = QGridLayout()
        
        row = 0
        for field in fields:
            value = data.get(field)
            if value:
                label = field.replace('_', ' ').replace('media', '1/2').title()
                layout.addWidget(QLabel(f"<b>{label}:</b>"), row, 0)
                layout.addWidget(QLabel(str(value)), row, 1)
                row += 1
        
        group.setLayout(layout)
        return group

    def create_image_display_group(self, title, section, field, data, field_name=None, additional_fields=None, svg_size=(150, 150)):
        group = QGroupBox(title)
        layout = QVBoxLayout()
        group.setLayout(layout)

        value = data.get(field_name or field)
        
        if not value or value.lower() == 'no':
            layout.addWidget(QLabel("NO"), alignment=Qt.AlignmentFlag.AlignCenter)
            return group

        svg_lookup_value = value
        display_value_label = True
        if field == 'modelo_chaleco' and value.lower() in ['si', 'true']:
            svg_lookup_value = 'Chaleco'
            display_value_label = False

        svg_path = self.get_svg_path(section, field, svg_lookup_value)
        svg_widget = self.create_svg_widget(svg_path, size=svg_size)
        
        if svg_widget:
            layout.addWidget(svg_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        
        if display_value_label:
            layout.addWidget(QLabel(value), alignment=Qt.AlignmentFlag.AlignCenter)
        
        if additional_fields:
            for label, data_key in additional_fields.items():
                if data_key in data and data[data_key]:
                    field_value = data[data_key]
                    display_value = field_value
                    if isinstance(field_value, str) and field_value.lower() in ['true', 'false']:
                        display_value = 'Sí' if field_value.lower() == 'true' else 'No'
                    
                    layout.addWidget(QLabel(f"<b>{label}:</b> {display_value}"), alignment=Qt.AlignmentFlag.AlignCenter)

        return group

    def create_pantalon_section(self):
        """Create the pantalon section with all details"""
        section_data = self.order_data['details']['pantalon']
        section_group = QGroupBox("MEDIDAS PANTALON")
        section_layout = QVBoxLayout()
        
        main_grid = QGridLayout()

        # Medidas
        medidas_group = self.create_data_group(
            "Medidas",
            section_data,
            ['CINTURA', 'BASE', 'LARGO', 'PIERNA', 'RODILLA', 'BOTA', 'TIRO', 'CONT T']
        )
        main_grid.addWidget(medidas_group, 0, 0, 2, 1)

        # Bolsillo Delantero
        bolsillo_del_group = self.create_image_display_group(
            "Bolsillo Delantero", 'pantalon', 'bolsillo_delantero', section_data,
            field_name='Bolsillo Delantero'
        )
        main_grid.addWidget(bolsillo_del_group, 0, 1)

        # Bolsillo Trasero
        bolsillo_tras_group = self.create_image_display_group(
            "Bolsillo Trasero", 'pantalon', 'bolsillo_trasero', section_data,
            field_name='Bolsillo Trasero'
        )
        main_grid.addWidget(bolsillo_tras_group, 0, 2)
        
        # Terminado Bolsillo Trasero
        terminado_bolsillo_group = self.create_data_group(
            "Terminado Bolsillo Trasero",
            section_data,
            ['terminado_bolsillo_trasero_boton', 'terminado_bolsillo_trasero_oreja', 'terminado_bolsillo_trasero_parche', 'terminado_bolsillo_trasero_parche_mod']
        )
        main_grid.addWidget(terminado_bolsillo_group, 1, 2)

        # Pretina
        pretina_group = self.create_image_display_group(
            "Pretina", 'pantalon', 'pretina', section_data,
            field_name='Pretina',
            additional_fields={
                'Botón': 'boton_pretina',
                'Gancho': 'gancho_pretina',
                'Pasadores': 'pasadores_pretina'
            }
        )
        main_grid.addWidget(pretina_group, 0, 3)

        # Forrado
        forrado_group = self.create_data_group(
            "Forrado",
            section_data,
            ['Forrado', 'forrado_opcion_1', 'forrado_opcion_2']
        )
        main_grid.addWidget(forrado_group, 1, 1)

        # Otros
        otros_group = self.create_data_group(
            "Otros",
            section_data,
            ['Especial', 'Relojera', 'Bota']
        )
        main_grid.addWidget(otros_group, 2, 0)
        
        # Estilo Delantero
        estilo_delantero_group = self.create_data_group(
            "Estilo Delantero",
            section_data,
            ['estilo_delantero']
        )
        main_grid.addWidget(estilo_delantero_group, 2, 1)

        # Vendedor
        vendedor_group = self.create_data_group(
            "Vendedor",
            section_data,
            ['vendedor']
        )
        main_grid.addWidget(vendedor_group, 2, 2)

        section_layout.addLayout(main_grid)
        
        # Observaciones
        if section_data.get('observaciones'):
            obs_group = QGroupBox("Observaciones")
            obs_layout = QVBoxLayout()
            obs_label = QLabel(section_data['observaciones'])
            obs_label.setWordWrap(True)
            obs_layout.addWidget(obs_label)
            obs_group.setLayout(obs_layout)
            section_layout.addWidget(obs_group)
        
        section_group.setLayout(section_layout)
        return section_group