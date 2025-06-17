from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QGroupBox, QScrollArea, QFrame)
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
            
        svg_paths = {
            'camisa': {
                'modelo_espalda': {
                    'tableta': f"{self.svg_base_path}/Modelo Espalda/Tableta_1.svg",
                    'prenses': f"{self.svg_base_path}/Modelo Espalda/Prenses_2.svg",
                    'fuelle': f"{self.svg_base_path}/Modelo Espalda/Fuelle_3.svg",
                    'doble tableta': f"{self.svg_base_path}/Modelo Espalda/Doble Tableta_4.svg",
                    'pinzas': f"{self.svg_base_path}/Modelo Espalda/Pinzas_5.svg",
                    'lisa': f"{self.svg_base_path}/Modelo Espalda/Lisa_6.svg"
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
                    'd uso': f"{self.svg_base_path}/Modelo Puño/D USO.svg",
                    'man': f"{self.svg_base_path}/Modelo Puño/MAN.svg",
                    'punta': f"{self.svg_base_path}/Modelo Puño/PUNTA.svg",
                    'ra': f"{self.svg_base_path}/Modelo Puño/RA.svg",
                    'ra2b': f"{self.svg_base_path}/Modelo Puño/RA2B.svg",
                    'rd': f"{self.svg_base_path}/Modelo Puño/RD.svg"
                }
            },
            'saco': {
                'modelo_chaleco': {
                    'chaleco': f"{self.svg_base_path}/Medidas Saco/Modelo chaleco/Chaleco.svg"
                },
                'bolsillo_superior': {
                    'aletilla': f"{self.svg_base_path}/Medidas Saco/Bolsillo superior/Aletilla.svg",
                    'parche': f"{self.svg_base_path}/Medidas Saco/Bolsillo superior/Parche.svg"
                },
                'bolsillo_inferior': {
                    '3er bolsillo': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/3er bolsillo.svg",
                    'aletilla': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Aletilla.svg",
                    'parche': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Parche.svg",
                    'ribete': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Ribete.svg",
                    'tapa cuadrada': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Tapa cuadrada.svg",
                    'tapa redonda': f"{self.svg_base_path}/Medidas Saco/Bolsillo inferior/Tapa redonda.svg"
                },
                'solapa': {
                    'Cuadrada': f"{self.svg_base_path}/Medidas Saco/Solapa/Cuadrada.svg",
                    'Redonda': f"{self.svg_base_path}/Medidas Saco/Solapa/Redonda.svg",
                    'En punta': f"{self.svg_base_path}/Medidas Saco/Solapa/En punta.svg"
                },
                'estilo': {
                    'cruzado': f"{self.svg_base_path}/Medidas Saco/Estilo/Cruzado.svg",
                    'sencillo': f"{self.svg_base_path}/Medidas Saco/Estilo/Sencillo.svg"
                }
            },
            'pantalon': {
                'bolsillo_delantero': {
                    'jean#1': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Jean 1.svg",
                    'jean#2': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Jean 2.svg",
                    'sesgado#3': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Sesgado 3.svg",
                    'ses. t recta': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/SES T RECTA 4.svg",
                    'ses. t curva': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/SES T CURVA 5.svg",
                    'allado#6': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Allado 6.svg",
                    'redondo#7': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Redondo 7.svg",
                    'italiano#8': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Italiano 8.svg",
                    'texas#9': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 9.svg",
                    'texas#10': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 10.svg",
                    'texas#11': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 11.svg",
                    'texas#12': f"{self.svg_base_path}/Medidas pantalon/Bolsillo delantero/Texas 12.svg"
                },
                'bolsillo_trasero': {
                    'tapa#1': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 1.svg",
                    'tapa#2': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 2.svg",
                    'tapa#3': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 3.svg",
                    'tapa#4': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 4.svg",
                    'tapa#5': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Tapa 5.svg",
                    'ribete': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Ribete.svg",
                    'aletilla': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Aletilla.svg",
                    'con oreja': f"{self.svg_base_path}/Medidas pantalon/Bolsillo trasero/Con oreja.svg"
                },
                'pretina': {
                    'recta': f"{self.svg_base_path}/Medidas pantalon/Pretina/Recta.svg",
                    'cruzada curva': f"{self.svg_base_path}/Medidas pantalon/Pretina/Cruzada curva.svg",
                    'cruzada recta': f"{self.svg_base_path}/Medidas pantalon/Pretina/Cruzada recta.svg",
                    'cruzada punta': f"{self.svg_base_path}/Medidas pantalon/Pretina/Cruzada punta.svg"
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
        
    def create_svg_widget(self, svg_path):
        """Create and return an SVG widget if the path exists"""
        if svg_path and os.path.exists(svg_path):
            svg_widget = QSvgWidget(svg_path)
            svg_widget.setFixedSize(300, 300)
            return svg_widget
        return None
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Ver Orden")
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
        info_layout = QVBoxLayout()
        
        info_layout.addWidget(QLabel(f"Número de Orden: {order_info['order_number']}"))
        info_layout.addWidget(QLabel(f"Cliente: {order_info['client_name']}"))
        info_layout.addWidget(QLabel(f"Fecha de Orden: {order_info['order_date']}"))
        info_layout.addWidget(QLabel(f"Fecha de Entrega: {order_info['delivery_date']}"))
        info_layout.addWidget(QLabel(f"Estado: {order_info['status']}"))
        if order_info.get('vendedor'):
            info_layout.addWidget(QLabel(f"Vendedor: {order_info['vendedor']}"))
        if order_info.get('observaciones'):
            info_layout.addWidget(QLabel(f"Observaciones: {order_info['observaciones']}"))
        
        info_group.setLayout(info_layout)
        self.layout.addWidget(info_group)
        
        # Financial Info
        financial_group = QGroupBox("Información Financiera")
        financial_layout = QVBoxLayout()
        
        financial_layout.addWidget(QLabel(f"Valor de la Orden: $ {order_info['order_value']:,}"))
        financial_layout.addWidget(QLabel(f"Abono: $ {order_info['deposit']:,}"))
        saldo = order_info['order_value'] - order_info['deposit']
        financial_layout.addWidget(QLabel(f"Saldo: $ {saldo:,}"))
        
        financial_group.setLayout(financial_layout)
        self.layout.addWidget(financial_group)
        
        # References
        references_group = QGroupBox("Referencias")
        references_layout = QVBoxLayout()
        
        for ref in self.order_data['references']:
            ref_layout = QHBoxLayout()
            ref_layout.addWidget(QLabel(f"Ref: {ref['reference']}"))
            ref_layout.addWidget(QLabel(f"Color: {ref['color']}"))
            ref_layout.addWidget(QLabel(f"Valor: $ {ref['value']:,}"))
            references_layout.addLayout(ref_layout)
        
        references_group.setLayout(references_layout)
        self.layout.addWidget(references_group)
        
        # Details Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        
        details_widget = QWidget()
        details_layout = QVBoxLayout(details_widget)
        
        # Add measurement sections with their corresponding images
        sections = {
            'camisa': 'Medidas Camisa',
            'saco': 'Medidas Saco',
            'pantalon': 'Medidas Pantalón'
        }
        
        for section_key, section_title in sections.items():
            if section_key in self.order_data['details']:
                section_group = QGroupBox(section_title)
                section_layout = QVBoxLayout()
                
                # Add model SVGs if available
                if section_key == 'camisa':
                    # Medidas básicas
                    medidas = [
                        'cuello_espalda', 'hombro', 'manga', 'x_cont', 'largo_cont',
                        'manga_pecho', 'cintura', 'cadera'
                    ]
                    for medida in medidas:
                        if medida in self.order_data['details'][section_key]:
                            field_layout = QHBoxLayout()
                            field_layout.addWidget(QLabel(f"{medida.replace('_', ' ').title()}:"))
                            field_layout.addWidget(QLabel(str(self.order_data['details'][section_key][medida])))
                            field_layout.addStretch()
                            section_layout.addLayout(field_layout)
                    
                    # Modelo Espalda
                    espalda_value = self.order_data['details'][section_key].get('modelo_espalda', '')
                    if espalda_value and espalda_value.lower() != 'no':
                        espalda_svg_path = self.get_svg_path(section_key, 'modelo_espalda', espalda_value)
                        espalda_svg = self.create_svg_widget(espalda_svg_path)
                        if espalda_svg:
                            section_layout.addWidget(QLabel("Modelo Espalda:"))
                            section_layout.addWidget(espalda_svg, alignment=Qt.AlignCenter)
                    
                    # Modelo Bolsillo
                    bolsillo_value = self.order_data['details'][section_key].get('modelo_bolsillo', '')
                    if bolsillo_value and bolsillo_value.lower() != 'no':
                        bolsillo_svg_path = self.get_svg_path(section_key, 'modelo_bolsillo', bolsillo_value)
                        bolsillo_svg = self.create_svg_widget(bolsillo_svg_path)
                        if bolsillo_svg:
                            section_layout.addWidget(QLabel("Modelo Bolsillo:"))
                            section_layout.addWidget(bolsillo_svg, alignment=Qt.AlignCenter)
                    
                    # Modelo Puño
                    puño_value = self.order_data['details'][section_key].get('modelo_puño', '')
                    if puño_value and puño_value.lower() != 'no':
                        puño_svg_path = self.get_svg_path(section_key, 'modelo_puño', puño_value)
                        puño_svg = self.create_svg_widget(puño_svg_path)
                        if puño_svg:
                            section_layout.addWidget(QLabel("Modelo Puño:"))
                            section_layout.addWidget(puño_svg, alignment=Qt.AlignCenter)
                        # Mostrar textura y ancho del puño
                        if 'textura_puño' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Textura Puño: {self.order_data['details'][section_key]['textura_puño']}"))
                        if 'ancho_puño' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Ancho Puño: {self.order_data['details'][section_key]['ancho_puño']} cm"))
                    
                    # Modelo Cuello
                    cuello_value = self.order_data['details'][section_key].get('modelo_cuello', '')
                    if cuello_value and cuello_value.lower() != 'no':
                        cuello_svg_path = self.get_svg_path(section_key, 'modelo_cuello', cuello_value)
                        cuello_svg = self.create_svg_widget(cuello_svg_path)
                        if cuello_svg:
                            section_layout.addWidget(QLabel("Modelo Cuello:"))
                            section_layout.addWidget(cuello_svg, alignment=Qt.AlignCenter)
                        # Mostrar textura del cuello
                        if 'textura_cuello' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Textura Cuello: {self.order_data['details'][section_key]['textura_cuello']}"))
                        # Mostrar plum y bottom down
                        if 'plum' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Plum: {self.order_data['details'][section_key]['plum']}"))
                        if 'bottom_down' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Bottom Down: {self.order_data['details'][section_key]['bottom_down']}"))
                    
                    # Sección Texto
                    if 'iniciales' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel("Sección Texto:"))
                        section_layout.addWidget(QLabel(f"Iniciales: {self.order_data['details'][section_key]['iniciales']}"))
                        section_layout.addWidget(QLabel(f"Color: {self.order_data['details'][section_key].get('color_texto', '')}"))
                        section_layout.addWidget(QLabel(f"Tipo: {self.order_data['details'][section_key].get('tipo_texto', '')}"))
                        section_layout.addWidget(QLabel(f"Bol: {self.order_data['details'][section_key].get('bol', '')}"))
                        section_layout.addWidget(QLabel(f"Fre: {self.order_data['details'][section_key].get('fre', '')}"))
                        section_layout.addWidget(QLabel(f"Puñ: {self.order_data['details'][section_key].get('puñ', '')}"))
                    
                    # Sección Falda
                    if 'color_falda' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel("Sección Falda:"))
                        section_layout.addWidget(QLabel(f"Color: {self.order_data['details'][section_key]['color_falda']}"))
                        section_layout.addWidget(QLabel(f"Marip: {self.order_data['details'][section_key].get('marip', '')}"))
                        section_layout.addWidget(QLabel(f"R Abert: {self.order_data['details'][section_key].get('r_abert', '')}"))
                    
                    # Sección Prenda
                    if 'tipo_prenda' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel("Sección Prenda:"))
                        section_layout.addWidget(QLabel(f"Tipo: {self.order_data['details'][section_key]['tipo_prenda']}"))
                    
                    # Sección Empaque
                    if 'tipo_empaque' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel("Sección Empaque:"))
                        section_layout.addWidget(QLabel(f"Tipo: {self.order_data['details'][section_key]['tipo_empaque']}"))
                    
                    # Contextura Física
                    if 'medida_espalda' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel("Contextura Física:"))
                        section_layout.addWidget(QLabel(f"Medida Espalda: {self.order_data['details'][section_key]['medida_espalda']}"))
                        section_layout.addWidget(QLabel(f"Medida Abdomen: {self.order_data['details'][section_key].get('medida_abdomen', '')}"))
                    
                    # Observaciones y Vendedor
                    if 'observaciones_camisa' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Observaciones: {self.order_data['details'][section_key]['observaciones_camisa']}"))
                    if 'vendedor_camisa' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Vendedor: {self.order_data['details'][section_key]['vendedor_camisa']}"))
                
                elif section_key == 'saco':
                    # Medidas básicas
                    medidas = [
                        'talle', 'largo', 'media_espalda', 'hombro', 'manga',
                        'pecho', 'cintura', 'cadera'
                    ]
                    for medida in medidas:
                        if medida in self.order_data['details'][section_key]:
                            field_layout = QHBoxLayout()
                            field_layout.addWidget(QLabel(f"{medida.replace('_', ' ').title()}:"))
                            field_layout.addWidget(QLabel(str(self.order_data['details'][section_key][medida])))
                            field_layout.addStretch()
                            section_layout.addLayout(field_layout)
                    
                    # Modelo Chaleco
                    chaleco_value = self.order_data['details'][section_key].get('modelo_chaleco', '')
                    if chaleco_value and chaleco_value.lower() != 'no':
                        chaleco_svg_path = self.get_svg_path(section_key, 'modelo_chaleco', chaleco_value)
                        chaleco_svg = self.create_svg_widget(chaleco_svg_path)
                        if chaleco_svg:
                            section_layout.addWidget(QLabel("Modelo Chaleco:"))
                            section_layout.addWidget(chaleco_svg, alignment=Qt.AlignCenter)
                        
                        # Medidas del chaleco
                        if 'diagonal_pecho' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Diagonal Pecho: {self.order_data['details'][section_key]['diagonal_pecho']}"))
                        if 'centro' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Centro: {self.order_data['details'][section_key]['centro']}"))
                        if 'largo_espalda' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Largo Espalda: {self.order_data['details'][section_key]['largo_espalda']}"))
                        if 'observaciones_chaleco' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Observaciones Chaleco: {self.order_data['details'][section_key]['observaciones_chaleco']}"))
                    
                    # Estilo
                    estilo_value = self.order_data['details'][section_key].get('estilo', '')
                    if estilo_value:
                        estilo_svg_path = self.get_svg_path(section_key, 'estilo', estilo_value)
                        estilo_svg = self.create_svg_widget(estilo_svg_path)
                        if estilo_svg:
                            section_layout.addWidget(QLabel("Estilo:"))
                            section_layout.addWidget(estilo_svg, alignment=Qt.AlignCenter)
                        # Mostrar cantidad de botones
                        if 'cant_boton' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Cantidad de Botones: {self.order_data['details'][section_key]['cant_boton']}"))
                    
                    # Bolsillo superior
                    bolsillo_sup_value = self.order_data['details'][section_key].get('bolsillo_superior', '')
                    if bolsillo_sup_value:
                        if bolsillo_sup_value.lower() != 'no':
                            bolsillo_sup_svg_path = self.get_svg_path(section_key, 'bolsillo_superior', bolsillo_sup_value)
                            bolsillo_sup_svg = self.create_svg_widget(bolsillo_sup_svg_path)
                            if bolsillo_sup_svg:
                                section_layout.addWidget(QLabel("Bolsillo Superior:"))
                                section_layout.addWidget(bolsillo_sup_svg, alignment=Qt.AlignCenter)
                        else:
                            section_layout.addWidget(QLabel("Bolsillo Superior: NO"))
                    
                    # Bolsillo inferior
                    bolsillo_inf_value = self.order_data['details'][section_key].get('bolsillo_inferior', '')
                    if bolsillo_inf_value:
                        bolsillo_inf_svg_path = self.get_svg_path(section_key, 'bolsillo_inferior', bolsillo_inf_value)
                        bolsillo_inf_svg = self.create_svg_widget(bolsillo_inf_svg_path)
                        if bolsillo_inf_svg:
                            section_layout.addWidget(QLabel("Bolsillo Inferior:"))
                            section_layout.addWidget(bolsillo_inf_svg, alignment=Qt.AlignCenter)
                    
                    # Solapa
                    solapa_value = self.order_data['details'][section_key].get('solapa', '')
                    if solapa_value:
                        solapa_svg_path = self.get_svg_path(section_key, 'solapa', solapa_value)
                        solapa_svg = self.create_svg_widget(solapa_svg_path)
                        if solapa_svg:
                            section_layout.addWidget(QLabel("Solapa:"))
                            section_layout.addWidget(solapa_svg, alignment=Qt.AlignCenter)
                        # Mostrar ojal solapa
                        if 'ojal_solapa' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Ojal Solapa: {self.order_data['details'][section_key]['ojal_solapa']}"))
                    
                    # Observaciones y Vendedor
                    if 'observaciones_saco' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Observaciones: {self.order_data['details'][section_key]['observaciones_saco']}"))
                    if 'vendedor_saco' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Vendedor: {self.order_data['details'][section_key]['vendedor_saco']}"))
                
                elif section_key == 'pantalon':
                    # Medidas básicas
                    medidas = [
                        'cintura', 'base', 'largo', 'pierna', 'rodilla',
                        'bota', 'tiro', 'cont_t'
                    ]
                    for medida in medidas:
                        if medida in self.order_data['details'][section_key]:
                            field_layout = QHBoxLayout()
                            field_layout.addWidget(QLabel(f"{medida.replace('_', ' ').title()}:"))
                            field_layout.addWidget(QLabel(str(self.order_data['details'][section_key][medida])))
                            field_layout.addStretch()
                            section_layout.addLayout(field_layout)
                    
                    # Bolsillo delantero
                    bolsillo_del_value = self.order_data['details'][section_key].get('bolsillo_delantero', '')
                    if bolsillo_del_value:
                        bolsillo_del_svg_path = self.get_svg_path(section_key, 'bolsillo_delantero', bolsillo_del_value)
                        bolsillo_del_svg = self.create_svg_widget(bolsillo_del_svg_path)
                        if bolsillo_del_svg:
                            section_layout.addWidget(QLabel("Bolsillo Delantero:"))
                            section_layout.addWidget(bolsillo_del_svg, alignment=Qt.AlignCenter)
                    
                    # Bolsillo trasero
                    bolsillo_tras_value = self.order_data['details'][section_key].get('bolsillo_trasero', '')
                    if bolsillo_tras_value:
                        bolsillo_tras_svg_path = self.get_svg_path(section_key, 'bolsillo_trasero', bolsillo_tras_value)
                        bolsillo_tras_svg = self.create_svg_widget(bolsillo_tras_svg_path)
                        if bolsillo_tras_svg:
                            section_layout.addWidget(QLabel("Bolsillo Trasero:"))
                            section_layout.addWidget(bolsillo_tras_svg, alignment=Qt.AlignCenter)
                        
                        # Terminado del bolsillo trasero
                        if 'boton_trasero' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Botón: {self.order_data['details'][section_key]['boton_trasero']}"))
                        if 'oreja_trasero' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Oreja: {self.order_data['details'][section_key]['oreja_trasero']}"))
                        if 'parche_trasero' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Parche: {self.order_data['details'][section_key]['parche_trasero']}"))
                        if 'mod_trasero' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"MOD#: {self.order_data['details'][section_key]['mod_trasero']}"))
                    
                    # Pretina
                    pretina_value = self.order_data['details'][section_key].get('pretina', '')
                    if pretina_value:
                        pretina_svg_path = self.get_svg_path(section_key, 'pretina', pretina_value)
                        pretina_svg = self.create_svg_widget(pretina_svg_path)
                        if pretina_svg:
                            section_layout.addWidget(QLabel("Pretina:"))
                            section_layout.addWidget(pretina_svg, alignment=Qt.AlignCenter)
                        
                        # Detalles de la pretina
                        if 'boton_pretina' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Botón: {self.order_data['details'][section_key]['boton_pretina']}"))
                        if 'gancho_pretina' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Gancho: {self.order_data['details'][section_key]['gancho_pretina']}"))
                        if 'pasadores_pretina' in self.order_data['details'][section_key]:
                            section_layout.addWidget(QLabel(f"Pasadores: {self.order_data['details'][section_key]['pasadores_pretina']}"))
                    
                    # Forrado
                    if 'forrado' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Forrado: {self.order_data['details'][section_key]['forrado']}"))
                    
                    # Especial
                    if 'texto_especial' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Texto Especial: {self.order_data['details'][section_key]['texto_especial']}"))
                    if 'relojera' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Relojera: {self.order_data['details'][section_key]['relojera']}"))
                    
                    # Bota
                    if 'bota' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Bota: {self.order_data['details'][section_key]['bota']}"))
                    
                    # Estilo delantero
                    if 'estilo_delantero' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Estilo Delantero: {self.order_data['details'][section_key]['estilo_delantero']}"))
                    
                    # Observaciones y Vendedor
                    if 'observaciones_pantalon' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Observaciones: {self.order_data['details'][section_key]['observaciones_pantalon']}"))
                    if 'vendedor_pantalon' in self.order_data['details'][section_key]:
                        section_layout.addWidget(QLabel(f"Vendedor: {self.order_data['details'][section_key]['vendedor_pantalon']}"))
                
                section_group.setLayout(section_layout)
                details_layout.addWidget(section_group)
        
        scroll.setWidget(details_widget)
        self.layout.addWidget(scroll)
        
        # Add stretch to push everything up
        self.layout.addStretch() 