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
                    'Jean #1': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Jean 1.svg",
                    'Jean #2': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Jean 2.svg",
                    'Sesgado #3': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Sesgado 3.svg",
                    'Ses. T Recta #4': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/SES T RECTA 4.svg",
                    'Ses. T Curva #5': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/SES T CURVA 5.svg",
                    'Allado #6': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Allado 6.svg",
                    'Redondo #7': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Redondo 7.svg",
                    'Italiano #8': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Italiano 8.svg",
                    'Texas #9': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Texas 9.svg",
                    'Texas #10': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Texas 10.svg",
                    'Texas #11': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Texas 11.svg",
                    'Texas #12': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Delantero/Texas 12.svg"
                },
                'bolsillo_trasero': {
                    'Tapa #1': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Tapa 1.svg",
                    'Tapa #2': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Tapa 2.svg",
                    'Tapa #3': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Tapa 3.svg",
                    'Tapa #4': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Tapa 4.svg",
                    'Tapa #5': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Tapa 5.svg",
                    'Ribete': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Ribete.svg",
                    'Aletilla': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Aletilla.svg",
                    'Con Oreja': f"{self.svg_base_path}/Medidas Pantalon/Bolsillo Trasero/Con oreja.svg"
                },
                'pretina': {
                    'Recta': f"{self.svg_base_path}/Medidas Pantalon/Pretina/Recta.svg",
                    'Cruzada Curva': f"{self.svg_base_path}/Medidas Pantalon/Pretina/Cruzada curva.svg",
                    'Cruzada Recta': f"{self.svg_base_path}/Medidas Pantalon/Pretina/Cruzada recta.svg",
                    'Cruzada Punta': f"{self.svg_base_path}/Medidas Pantalon/Pretina/Cruzada punta.svg"
                }
            }
        }
        
        try:
            # Normalizar el valor para la búsqueda
            normalized_value = value.strip()
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
        self.layout = QVBoxLayout(self)
        
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
        
        self.layout.addLayout(header_layout)
        
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
        self.layout.addWidget(info_group)
        
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
        self.layout.addWidget(financial_group)
        
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
            self.layout.addWidget(references_group)
        
        # Details Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        
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
        self.layout.addWidget(scroll, 1)
        
        # Add some spacing at the bottom
        self.layout.addStretch()
    
    def create_camisa_section(self):
        """Create the camisa section with all details"""
        section_data = self.order_data['details']['camisa']
        section_group = QGroupBox("MEDIDAS CAMISA")
        section_layout = QVBoxLayout()
        
        # Medidas Básicas
        medidas_group = QGroupBox("Medidas")
        medidas_layout = QGridLayout()
        
        # Lista de todas las medidas posibles
        medidas = [
            'cuello', 'espalda', 'hombro', 'manga_x_cont', 'largo',
            'cont_manga', 'pecho', 'cintura', 'cadera'
        ]
        
        row, col = 0, 0
        for medida in medidas:
            if medida in section_data:
                medidas_layout.addWidget(QLabel(f"{medida.replace('_', ' ').title()}:"), row, col*2)
                medidas_layout.addWidget(QLabel(section_data[medida]), row, col*2+1)
                col = (col + 1) % 3
                if col == 0:
                    row += 1
        
        medidas_group.setLayout(medidas_layout)
        section_layout.addWidget(medidas_group)
        
        # Modelo Espalda
        espalda_value = section_data.get('modelo_espalda', '')
        espalda_group = QGroupBox("Modelo Espalda")
        espalda_layout = QVBoxLayout()
        
        if espalda_value and espalda_value.lower() != 'no':
            espalda_svg_path = self.get_svg_path('camisa', 'modelo_espalda', espalda_value)
            espalda_svg = self.create_svg_widget(espalda_svg_path, (200, 200))
            if espalda_svg:
                espalda_layout.addWidget(espalda_svg, alignment=Qt.AlignCenter)
            espalda_layout.addWidget(QLabel(espalda_value), alignment=Qt.AlignCenter)
        else:
            espalda_layout.addWidget(QLabel("NO"), alignment=Qt.AlignCenter)
        
        # Opciones adicionales
        if 'prespuente' in section_data:
            espalda_layout.addWidget(QLabel(f"Prespuente: {section_data['prespuente']}"))
        if 'pechera' in section_data:
            espalda_layout.addWidget(QLabel(f"Pechera: {'Sí' if section_data['pechera'].lower() == 'true' else 'No'}"))
        if 'tapa_boton' in section_data:
            espalda_layout.addWidget(QLabel(f"Tapa Botón: {'Sí' if section_data['tapa_boton'].lower() == 'true' else 'No'}"))
        
        espalda_group.setLayout(espalda_layout)
        section_layout.addWidget(espalda_group)
        
        # Modelo Bolsillo
        bolsillo_value = section_data.get('modelo_bolsillo', '')
        bolsillo_group = QGroupBox("Modelo Bolsillo")
        bolsillo_layout = QVBoxLayout()
        #quitar los saltos de linea
        bolsillo_value = bolsillo_value.replace('\n', ' ')
        if bolsillo_value and bolsillo_value.lower() != 'no':
            bolsillo_svg_path = self.get_svg_path('camisa', 'modelo_bolsillo', bolsillo_value)
            bolsillo_svg = self.create_svg_widget(bolsillo_svg_path, (150, 150))
            if bolsillo_svg:
                bolsillo_layout.addWidget(bolsillo_svg, alignment=Qt.AlignCenter)
            bolsillo_layout.addWidget(QLabel(bolsillo_value), alignment=Qt.AlignCenter)
            
            # Detalles adicionales del bolsillo
            if 'lado_bolsillo' in section_data:
                bolsillo_layout.addWidget(QLabel(f"Lado: {section_data['lado_bolsillo']}"))
            if 'cantidad_bolsillo' in section_data:
                bolsillo_layout.addWidget(QLabel(f"Cantidad: {section_data['cantidad_bolsillo']}"))
        else:
            bolsillo_layout.addWidget(QLabel("NO"), alignment=Qt.AlignCenter)
        
        bolsillo_group.setLayout(bolsillo_layout)
        section_layout.addWidget(bolsillo_group)
        
        # Modelo Puño
        puno_group = QGroupBox("Modelo Puño")
        puno_layout = QVBoxLayout()
        
        puno_value = section_data.get('modelo_puno', '')
        if puno_value and puno_value.lower() != 'no':
            puno_svg_path = self.get_svg_path('camisa', 'modelo_puño', puno_value)
            puno_svg = self.create_svg_widget(puno_svg_path, (150, 150))
            if puno_svg:
                puno_layout.addWidget(puno_svg, alignment=Qt.AlignCenter)
            puno_layout.addWidget(QLabel(puno_value), alignment=Qt.AlignCenter)
            
            # Textura y ancho del puño
            if 'textura_puno' in section_data:
                puno_layout.addWidget(QLabel(f"Textura: {section_data['textura_puno']}"))
            if 'ancho_puno' in section_data:
                puno_layout.addWidget(QLabel(f"Ancho: {section_data['ancho_puno']} cm"))
        else:
            puno_layout.addWidget(QLabel("NO"), alignment=Qt.AlignCenter)
        
        puno_group.setLayout(puno_layout)
        section_layout.addWidget(puno_group)
        
        # Modelo Cuello
        cuello_group = QGroupBox("Modelo Cuello")
        cuello_layout = QVBoxLayout()
        
        cuello_value = section_data.get('modelo_cuello', '')
        if cuello_value and cuello_value.lower() != 'no':
            cuello_layout.addWidget(QLabel(cuello_value), alignment=Qt.AlignCenter)
            
            # Textura y opciones adicionales
            if 'textura_cuello' in section_data:
                cuello_layout.addWidget(QLabel(f"Textura: {section_data['textura_cuello']}"))
                print(section_data['textura_cuello'])
            if 'plum' in section_data:
                cuello_layout.addWidget(QLabel(f"Plum: {section_data['plum']}"))
                print(section_data['plum'])
            if 'bd' in section_data:
                cuello_layout.addWidget(QLabel(f"Bottom Down: {section_data['bd']}"))
                print(section_data['bd'])
        else:
            cuello_layout.addWidget(QLabel("NO"), alignment=Qt.AlignCenter)
        
        cuello_group.setLayout(cuello_layout)
        section_layout.addWidget(cuello_group)
        
        # Texto
        if 'iniciales' in section_data:
            texto_group = QGroupBox("Texto")
            texto_layout = QGridLayout()
            
            campos = ['iniciales', 'color', 'tipo', 'bol', 'fre', 'pun']
            row, col = 0, 0
            for campo in campos:
                if campo in section_data:
                    texto_layout.addWidget(QLabel(campo.title() + ":"), row, col*2)
                    texto_layout.addWidget(QLabel(section_data[campo]), row, col*2+1)
                    col = (col + 1) % 3
                    if col == 0:
                        row += 1
            
            texto_group.setLayout(texto_layout)
            section_layout.addWidget(texto_group)
        
        # Falda
        if 'color_falda' in section_data:
            falda_group = QGroupBox("Falda")
            falda_layout = QGridLayout()
            
            campos = ['color_falda', 'marip', 'r_abert']
            row, col = 0, 0
            for campo in campos:
                if campo in section_data:
                    falda_layout.addWidget(QLabel(campo.replace('_', ' ').title() + ":"), row, col*2)
                    falda_layout.addWidget(QLabel(section_data[campo]), row, col*2+1)
                    col = (col + 1) % 2
                    if col == 0:
                        row += 1
            
            falda_group.setLayout(falda_layout)
            section_layout.addWidget(falda_group)
        
        # Prenda y Empaque
        if 'tipo_prenda' in section_data or 'tipo_empaque' in section_data:
            pe_group = QGroupBox("Prenda y Empaque")
            pe_layout = QGridLayout()
            
            row = 0
            if 'tipo_prenda' in section_data:
                pe_layout.addWidget(QLabel("Prenda:"), row, 0)
                pe_layout.addWidget(QLabel(section_data['tipo_prenda']), row, 1)
                row += 1
            if 'tipo_empaque' in section_data:
                pe_layout.addWidget(QLabel("Empaque:"), row, 0)
                pe_layout.addWidget(QLabel(section_data['tipo_empaque']), row, 1)
            
            pe_group.setLayout(pe_layout)
            section_layout.addWidget(pe_group)
        
        # Contextura Física
        if 'espalda' in section_data or 'abdomen' in section_data:
            contextura_group = QGroupBox("Contextura Física")
            contextura_layout = QGridLayout()
            
            row = 0
            if 'espalda' in section_data:
                contextura_layout.addWidget(QLabel("Espalda:"), row, 0)
                contextura_layout.addWidget(QLabel(section_data['espalda']), row, 1)
                row += 1
            if 'abdomen' in section_data:
                contextura_layout.addWidget(QLabel("Abdomen:"), row, 0)
                contextura_layout.addWidget(QLabel(section_data['abdomen']), row, 1)
            
            contextura_group.setLayout(contextura_layout)
            section_layout.addWidget(contextura_group)
        
        # Observaciones
        if 'observaciones' in section_data:
            obs_group = QGroupBox("Observaciones")
            obs_layout = QVBoxLayout()
            obs_layout.addWidget(QLabel(section_data['observaciones']))
            obs_group.setLayout(obs_layout)
            section_layout.addWidget(obs_group)
        
        section_group.setLayout(section_layout)
        return section_group
    
    def create_saco_section(self):
        """Create the saco section with all details"""
        section_data = self.order_data['details']['saco']
        section_group = QGroupBox("MEDIDAS SACO")
        section_layout = QVBoxLayout()
        
        # Medidas Básicas
        medidas_group = QGroupBox("Medidas")
        medidas_layout = QGridLayout()
        
        medidas = [
            'talle', 'largo', 'media_espalda', 'hombro', 'manga',
            'pecho', 'cintura', 'cadera'
        ]
        
        row, col = 0, 0
        for medida in medidas:
            if medida in section_data:
                medidas_layout.addWidget(QLabel(f"{medida.replace('_', ' ').title()}:"), row, col*2)
                medidas_layout.addWidget(QLabel(section_data[medida]), row, col*2+1)
                col = (col + 1) % 3
                if col == 0:
                    row += 1
        
        medidas_group.setLayout(medidas_layout)
        section_layout.addWidget(medidas_group)
        
        # Estilo
        estilo_value = section_data.get('estilo', '')
        estilo_group = QGroupBox("Estilo")
        estilo_layout = QVBoxLayout()
        
        if estilo_value:
            estilo_svg_path = self.get_svg_path('saco', 'estilo', estilo_value)
            estilo_svg = self.create_svg_widget(estilo_svg_path, (200, 200))
            if estilo_svg:
                estilo_layout.addWidget(estilo_svg, alignment=Qt.AlignCenter)
            estilo_layout.addWidget(QLabel(estilo_value), alignment=Qt.AlignCenter)
            
            if 'cant_boton' in section_data:
                estilo_layout.addWidget(QLabel(f"Cant. Botón: {section_data['cant_boton']}"))
        
        estilo_group.setLayout(estilo_layout)
        section_layout.addWidget(estilo_group)
        
        # Solapa
        solapa_value = section_data.get('solapa', '')
        solapa_group = QGroupBox("Solapa")
        solapa_layout = QVBoxLayout()
        
        if solapa_value:
            solapa_svg_path = self.get_svg_path('saco', 'solapa', solapa_value)
            solapa_svg = self.create_svg_widget(solapa_svg_path, (150, 150))
            if solapa_svg:
                solapa_layout.addWidget(solapa_svg, alignment=Qt.AlignCenter)
            solapa_layout.addWidget(QLabel(solapa_value), alignment=Qt.AlignCenter)
            
            if 'ojal_solapa' in section_data:
                solapa_layout.addWidget(QLabel(f"Ojal Solapa: {'Sí' if section_data['ojal_solapa'].lower() == 'true' else 'No'}"))
        
        solapa_group.setLayout(solapa_layout)
        section_layout.addWidget(solapa_group)
        
        # Bolsillo Inferior
        bolsillo_inf_value = section_data.get('bolsillo_inferior', '')
        bolsillo_inf_group = QGroupBox("Bolsillo Inferior")
        bolsillo_inf_layout = QVBoxLayout()
        
        if bolsillo_inf_value:
            bolsillo_inf_svg_path = self.get_svg_path('saco', 'bolsillo_inferior', bolsillo_inf_value)
            bolsillo_inf_svg = self.create_svg_widget(bolsillo_inf_svg_path, (150, 150))
            if bolsillo_inf_svg:
                bolsillo_inf_layout.addWidget(bolsillo_inf_svg, alignment=Qt.AlignCenter)
            bolsillo_inf_layout.addWidget(QLabel(bolsillo_inf_value), alignment=Qt.AlignCenter)
        
        bolsillo_inf_group.setLayout(bolsillo_inf_layout)
        section_layout.addWidget(bolsillo_inf_group)
        
        # Bolsillo Superior
        bolsillo_sup_value = section_data.get('bolsillo_superior', '')
        bolsillo_sup_group = QGroupBox("Bolsillo Superior")
        bolsillo_sup_layout = QVBoxLayout()
        
        if bolsillo_sup_value:
            if bolsillo_sup_value.lower() == 'no':
                bolsillo_sup_layout.addWidget(QLabel("NO"), alignment=Qt.AlignCenter)
            else:
                bolsillo_sup_svg_path = self.get_svg_path('saco', 'bolsillo_superior', bolsillo_sup_value)
                bolsillo_sup_svg = self.create_svg_widget(bolsillo_sup_svg_path, (150, 150))
                if bolsillo_sup_svg:
                    bolsillo_sup_layout.addWidget(bolsillo_sup_svg, alignment=Qt.AlignCenter)
                bolsillo_sup_layout.addWidget(QLabel(bolsillo_sup_value), alignment=Qt.AlignCenter)
        
        bolsillo_sup_group.setLayout(bolsillo_sup_layout)
        section_layout.addWidget(bolsillo_sup_group)
        
        # Modelo Chaleco
        chaleco_value = section_data.get('modelo_chaleco', '')
        chaleco_group = QGroupBox("Modelo Chaleco")
        chaleco_layout = QVBoxLayout()
        
        if chaleco_value:
            if chaleco_value.lower() == 'no':
                chaleco_layout.addWidget(QLabel("NO"), alignment=Qt.AlignCenter)
            else:
                chaleco_svg_path = self.get_svg_path('saco', 'modelo_chaleco', chaleco_value)
                chaleco_svg = self.create_svg_widget(chaleco_svg_path, (200, 200))
                if chaleco_svg:
                    chaleco_layout.addWidget(chaleco_svg, alignment=Qt.AlignCenter)
                chaleco_layout.addWidget(QLabel(chaleco_value), alignment=Qt.AlignCenter)
                
                # Medidas del chaleco
                if 'diagonal_pecho' in section_data:
                    chaleco_layout.addWidget(QLabel(f"Diagonal Pecho: {section_data['diagonal_pecho']}"))
                if 'centro' in section_data:
                    chaleco_layout.addWidget(QLabel(f"Centro: {section_data['centro']}"))
                if 'largo_espalda' in section_data:
                    chaleco_layout.addWidget(QLabel(f"Largo Espalda: {section_data['largo_espalda']}"))
                if 'observaciones_chaleco' in section_data:
                    chaleco_layout.addWidget(QLabel(f"Observaciones: {section_data['observaciones_chaleco']}"))
        
        chaleco_group.setLayout(chaleco_layout)
        section_layout.addWidget(chaleco_group)
        
        # Observaciones
        if 'observaciones' in section_data:
            obs_group = QGroupBox("Observaciones")
            obs_layout = QVBoxLayout()
            obs_layout.addWidget(QLabel(section_data['observaciones']))
            obs_group.setLayout(obs_layout)
            section_layout.addWidget(obs_group)
        
        section_group.setLayout(section_layout)
        return section_group
    
    def create_pantalon_section(self):
        """Create the pantalon section with all details"""
        section_data = self.order_data['details']['pantalon']
        section_group = QGroupBox("MEDIDAS PANTALON")
        section_layout = QVBoxLayout()
        
        # Medidas Básicas
        medidas_group = QGroupBox("Medidas")
        medidas_layout = QGridLayout()
        
        medidas = [
            'cintura', 'base', 'largo', 'pierna', 'rodilla',
            'bota', 'tiro', 'cont_t'
        ]
        
        row, col = 0, 0
        for medida in medidas:
            if medida in section_data:
                medidas_layout.addWidget(QLabel(f"{medida.replace('_', ' ').title()}:"), row, col*2)
                medidas_layout.addWidget(QLabel(section_data[medida]), row, col*2+1)
                col = (col + 1) % 3
                if col == 0:
                    row += 1
        
        medidas_group.setLayout(medidas_layout)
        section_layout.addWidget(medidas_group)
        
        # Bolsillo Delantero
        bolsillo_del_value = section_data.get('bolsillo_delantero', '')
        bolsillo_del_group = QGroupBox("Bolsillo Delantero")
        bolsillo_del_layout = QVBoxLayout()
        
        if bolsillo_del_value:
            bolsillo_del_svg_path = self.get_svg_path('pantalon', 'bolsillo_delantero', bolsillo_del_value)
            bolsillo_del_svg = self.create_svg_widget(bolsillo_del_svg_path, (150, 150))
            if bolsillo_del_svg:
                bolsillo_del_layout.addWidget(bolsillo_del_svg, alignment=Qt.AlignCenter)
            bolsillo_del_layout.addWidget(QLabel(bolsillo_del_value), alignment=Qt.AlignCenter)
        
        bolsillo_del_group.setLayout(bolsillo_del_layout)
        section_layout.addWidget(bolsillo_del_group)
        
        # Bolsillo Trasero
        bolsillo_tras_value = section_data.get('bolsillo_trasero', '')
        bolsillo_tras_group = QGroupBox("Bolsillo Trasero")
        bolsillo_tras_layout = QVBoxLayout()
        
        if bolsillo_tras_value:
            bolsillo_tras_svg_path = self.get_svg_path('pantalon', 'bolsillo_trasero', bolsillo_tras_value)
            bolsillo_tras_svg = self.create_svg_widget(bolsillo_tras_svg_path, (150, 150))
            if bolsillo_tras_svg:
                bolsillo_tras_layout.addWidget(bolsillo_tras_svg, alignment=Qt.AlignCenter)
            bolsillo_tras_layout.addWidget(QLabel(bolsillo_tras_value), alignment=Qt.AlignCenter)
            
            # Terminado del bolsillo trasero
            terminado_layout = QGridLayout()
            if 'boton_trasero' in section_data:
                terminado_layout.addWidget(QLabel("Botón:"), 0, 0)
                terminado_layout.addWidget(QLabel(section_data['boton_trasero']), 0, 1)
            if 'oreja_trasero' in section_data:
                terminado_layout.addWidget(QLabel("Oreja:"), 1, 0)
                terminado_layout.addWidget(QLabel(section_data['oreja_trasero']), 1, 1)
            if 'parche_trasero' in section_data:
                terminado_layout.addWidget(QLabel("Parche:"), 2, 0)
                terminado_layout.addWidget(QLabel(section_data['parche_trasero']), 2, 1)
            if 'mod_trasero' in section_data:
                terminado_layout.addWidget(QLabel("MOD#:"), 3, 0)
                terminado_layout.addWidget(QLabel(section_data['mod_trasero']), 3, 1)
            
            if terminado_layout.count() > 0:
                bolsillo_tras_layout.addLayout(terminado_layout)
        
        bolsillo_tras_group.setLayout(bolsillo_tras_layout)
        section_layout.addWidget(bolsillo_tras_group)
        
        # Pretina
        pretina_value = section_data.get('pretina', '')
        pretina_group = QGroupBox("Pretina")
        pretina_layout = QVBoxLayout()
        
        if pretina_value:
            pretina_svg_path = self.get_svg_path('pantalon', 'pretina', pretina_value)
            pretina_svg = self.create_svg_widget(pretina_svg_path, (150, 150))
            if pretina_svg:
                pretina_layout.addWidget(pretina_svg, alignment=Qt.AlignCenter)
            pretina_layout.addWidget(QLabel(pretina_value), alignment=Qt.AlignCenter)
            
            # Detalles de la pretina
            if 'boton_pretina' in section_data:
                pretina_layout.addWidget(QLabel(f"Botón: {'Sí' if section_data['boton_pretina'].lower() == 'true' else 'No'}"))
            if 'gancho_pretina' in section_data:
                pretina_layout.addWidget(QLabel(f"Gancho: {'Sí' if section_data['gancho_pretina'].lower() == 'true' else 'No'}"))
            if 'pasadores_pretina' in section_data:
                pretina_layout.addWidget(QLabel(f"Pasadores: {section_data['pasadores_pretina']}"))
        
        pretina_group.setLayout(pretina_layout)
        section_layout.addWidget(pretina_group)
        
        # Forrado
        if 'forrado' in section_data:
            forrado_group = QGroupBox("Forrado")
            forrado_layout = QVBoxLayout()
            forrado_layout.addWidget(QLabel(section_data['forrado']))
            forrado_group.setLayout(forrado_layout)
            section_layout.addWidget(forrado_group)
        
        # Especial
        if 'texto_especial' in section_data or 'relojera' in section_data:
            especial_group = QGroupBox("Especial")
            especial_layout = QGridLayout()
            
            row = 0
            if 'texto_especial' in section_data:
                especial_layout.addWidget(QLabel("Texto:"), row, 0)
                especial_layout.addWidget(QLabel(section_data['texto_especial']), row, 1)
                row += 1
            if 'relojera' in section_data:
                especial_layout.addWidget(QLabel("Relojera:"), row, 0)
                especial_layout.addWidget(QLabel(section_data['relojera']), row, 1)
            
            especial_group.setLayout(especial_layout)
            section_layout.addWidget(especial_group)
        
        # Bota
        if 'bota' in section_data:
            bota_group = QGroupBox("Bota")
            bota_layout = QVBoxLayout()
            bota_layout.addWidget(QLabel(section_data['bota']))
            bota_group.setLayout(bota_layout)
            section_layout.addWidget(bota_group)
        
        # Estilo Delantero
        if 'estilo_delantero' in section_data:
            estilo_group = QGroupBox("Estilo Delantero")
            estilo_layout = QVBoxLayout()
            estilo_layout.addWidget(QLabel(section_data['estilo_delantero']))
            estilo_group.setLayout(estilo_layout)
            section_layout.addWidget(estilo_group)
        
        # Observaciones
        if 'observaciones' in section_data:
            obs_group = QGroupBox("Observaciones")
            obs_layout = QVBoxLayout()
            obs_layout.addWidget(QLabel(section_data['observaciones']))
            obs_group.setLayout(obs_layout)
            section_layout.addWidget(obs_group)
        
        section_group.setLayout(section_layout)
        return section_group