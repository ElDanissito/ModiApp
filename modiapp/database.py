import sqlite3
from datetime import datetime
import os
import sys

class Database:
    def __init__(self):
        # Get the directory where the executable or script is located
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            base_path = os.path.dirname(sys.executable)
        else:
            # Running as script
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Create data directory in the same location as the executable/script
        data_dir = os.path.join(base_path, 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        db_path = os.path.join(data_dir, 'orders.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Initialize the database and create tables if they don't exist"""
        # Create data directory if it doesn't exist
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        data_dir = os.path.join(base_path, 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        # Tabla de órdenes
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_number TEXT UNIQUE,
                client_name TEXT,
                order_date TEXT,
                delivery_date TEXT,
                status TEXT,
                order_value REAL,
                deposit REAL
            )
        ''')
        
        # Tabla de detalles de la orden
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_details (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                section TEXT,
                field TEXT,
                value TEXT,
                FOREIGN KEY (order_id) REFERENCES orders (id)
            )
        ''')
        
        # Tabla de referencias
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_references (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                reference TEXT,
                color TEXT,
                value REAL,
                FOREIGN KEY (order_id) REFERENCES orders (id)
            )
        ''')
        
        # Crear índices para mejorar el rendimiento
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_details_order_id ON order_details(order_id)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_references_order_id ON order_references(order_id)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_order_number ON orders(order_number)')
        
        self.conn.commit()

    def get_next_order_number(self):
        """Get the next available order number"""
        self.cursor.execute("SELECT MAX(order_number) FROM orders")
        last_number = self.cursor.fetchone()[0]
        
        if last_number is None:
            return "0000"
        
        next_number = int(last_number) + 1
        return f"{next_number:04d}"

    def create_order(self, data_package):
        """Create a new order with its details and references"""
        try:
            order_data = data_package['order_data']
            details_data = data_package['details']
            references = data_package['references']
            
            # Insertar la orden principal
            self.cursor.execute('''
                INSERT INTO orders (
                    order_number, client_name, order_date, delivery_date,
                    status, order_value, deposit    
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                order_data['order_number'],
                order_data['client_name'],
                order_data['order_date'],
                order_data['delivery_date'],
                order_data['status'],
                order_data['order_value'],
                order_data['deposit']
            ))
            
            order_id = self.cursor.lastrowid
            
            # Insertar detalles de la orden
            for section, fields in details_data.items():
                for field, value in fields.items():
                    if value:  # Solo guardar si hay un valor
                        self.cursor.execute('''
                            INSERT INTO order_details (order_id, section, field, value)
                            VALUES (?, ?, ?, ?)
                        ''', (order_id, section, field, str(value)))
            
            # Insertar referencias
            for ref in references:
                self.cursor.execute('''
                    INSERT INTO order_references (order_id, reference, color, value)
                    VALUES (?, ?, ?, ?)
                ''', (order_id, ref['reference'], ref['color'], ref['value']))
            
            self.conn.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"Error creating order: {e}")
            self.conn.rollback()
            return False

    def get_filtered_orders(self, estado=None, fecha_desde=None, fecha_hasta=None, search_text=None):
        """Get orders filtered by status, date range and search text"""
        query = "SELECT * FROM orders WHERE 1=1"
        params = []
        
        if estado:
            query += " AND status = ?"
            params.append(estado)
            
        if fecha_desde:
            query += " AND order_date >= ?"
            params.append(fecha_desde)
            
        if fecha_hasta:
            query += " AND order_date <= ?"
            params.append(fecha_hasta)
            
        if search_text:
            query += " AND (client_name LIKE ? OR order_number LIKE ?)"
            params.extend([f"%{search_text}%", f"%{search_text}%"])
            
        query += " ORDER BY order_date DESC LIMIT 20"
        
        self.cursor.execute(query, params)
        columns = [description[0] for description in self.cursor.description]
        orders = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        
        return orders

    def get_order_details(self, order_id):
        """Get all details for a specific order"""
        try:
            # Obtener información de la orden
            self.cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
            order = dict(zip([col[0] for col in self.cursor.description], self.cursor.fetchone()))
            
            # Obtener detalles de la orden
            self.cursor.execute('SELECT section, field, value FROM order_details WHERE order_id = ?', (order_id,))
            details = {}
            for section, field, value in self.cursor.fetchall():
                if section not in details:
                    details[section] = {}
                details[section][field] = value
            
            # Obtener referencias
            self.cursor.execute('SELECT reference, color, value FROM order_references WHERE order_id = ?', (order_id,))
            references = [{'reference': ref[0], 'color': ref[1], 'value': ref[2]} for ref in self.cursor.fetchall()]
            
            return {
                'order': order,
                'details': details,
                'references': references
            }
            
        except sqlite3.Error as e:
            print(f"Error getting order details: {e}")
            return None

    def get_order_by_number(self, order_number):
        """Get order details by order number"""
        try:
            self.cursor.execute('SELECT id FROM orders WHERE order_number = ?', (order_number,))
            result = self.cursor.fetchone()
            if result:
                return self.get_order_details(result[0])
            return None
        except sqlite3.Error as e:
            print(f"Error getting order by number: {e}")
            return None

    def update_order_status(self, order_id, new_status):
        """Update the status of a specific order"""
        try:
            self.cursor.execute('''
                UPDATE orders
                SET status = ?
                WHERE id = ?
            ''', (new_status, order_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating order status: {e}")
            self.conn.rollback()
            return False

    def delete_order(self, order_id):
        """Deletes an order and all its related details."""
        try:
            # Foreign key constraints should handle cascading deletes if set up,
            # but we delete explicitly from child tables for safety.
            self.cursor.execute('DELETE FROM order_details WHERE order_id = ?', (order_id,))
            self.cursor.execute('DELETE FROM order_references WHERE order_id = ?', (order_id,))
            self.cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error during deletion: {e}")
            return False

    def update_order_deposit(self, order_id, new_deposit):
        """Updates the deposit for a given order."""
        try:
            self.cursor.execute("UPDATE orders SET deposit = ? WHERE id = ?", (new_deposit, order_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def close(self):
        """Closes the database connection."""
        self.conn.close() 